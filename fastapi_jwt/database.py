from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


database_url = "postgresql://postgres:test123@localhost:5432/Users"

engine = create_engine(database_url)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()