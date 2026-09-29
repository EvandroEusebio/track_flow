from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

engine = create_engine(f'postgresql+psycopg://{os.getenv("POSTGRES_USER")}:{os.getenv("POSTGRES_PASSWORD")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("POSTGRES_DB")}', echo=True)

print("Database connection established.")

with Session(engine) as session:
    pass