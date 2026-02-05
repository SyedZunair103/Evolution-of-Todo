from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import tasks
from .api.auth import router as auth_router
import os
from dotenv import load_dotenv
from .logging_config import logger
from .database.connection import engine
from .models.task import Task  # Import all models to register them with SQLModel
from .models.user import User  # Import User model to register with SQLModel
from sqlmodel import SQLModel

load_dotenv()

app = FastAPI(title="Todo API", version="1.0.0")

# CORS configuration
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    os.getenv("NEXT_PUBLIC_BETTER_AUTH_URL", "http://localhost:3000"),
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    # Expose authorization header for JWT
    expose_headers=["Access-Control-Allow-Origin", "Authorization"]
)

# Include API routes
app.include_router(tasks.router, prefix="/api", tags=["tasks"])
app.include_router(auth_router, prefix="/api", tags=["auth"])

@app.get("/")
def read_root():
    return {"message": "Todo API is running!"}

@app.on_event("startup")
def on_startup():
    logger.info("Creating database tables...")
    SQLModel.metadata.create_all(bind=engine)
    logger.info("Database tables created successfully!")

    # Initialize demo users in the database to match the in-memory store
    from .models.user import User
    from sqlmodel import Session, select
    from .api.auth import demo_users

    with Session(engine) as session:
        for email, user_data in demo_users.items():
            existing_user = session.exec(select(User).where(User.email == email)).first()
            if not existing_user:
                db_user = User(
                    id=user_data["id"],
                    email=user_data["email"],
                    name=user_data["name"]
                )
                session.add(db_user)
                logger.info(f"Added demo user {email} to database")

        session.commit()
        logger.info("Demo users synchronized with database")

@app.get("/health")
def health_check():
    logger.info("Health check endpoint accessed")
    return {"status": "healthy"}