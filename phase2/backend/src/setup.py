from setuptools import setup, find_packages

setup(
    name="todo-backend",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi==0.104.1",
        "uvicorn[standard]==0.24.0",
        "sqlmodel==0.0.32",
        "pydantic==2.12.5",
        "python-jose[cryptography]==3.3.0",
        "python-multipart==0.0.6",
        "python-dotenv>=1.0.0",
        "pydantic-settings==2.1.0",
        "better-exceptions==0.3.3",
        "asyncpg==0.29.0"
    ],
    author="Todo App Team",
    description="Todo app backend API",
)