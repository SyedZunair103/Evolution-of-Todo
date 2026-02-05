from sqlmodel import create_engine
from sqlalchemy import MetaData
import os
from dotenv import load_dotenv

load_dotenv()

# Get database URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./todo_app.db")

if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Create engine
engine = create_engine(
    DATABASE_URL, 
    echo=True,
    pool_pre_ping=True  # Ye connection drop hone se bachata hai
)

# Create metadata instance
metadata = MetaData()