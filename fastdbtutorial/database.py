#database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:broletto@192.168.1.101/tutorial"

engine = create_engine(SQLALCHEMY_DATABASE_URL  , echo=True)

#Each instance of SessionLocal class will be  database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#we use declarative_base to return a class which we will inherit from to create database models or classes
Base = declarative_base()
