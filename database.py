import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean


DB_URL = 'localhost'
DB_password = 'password'
db_user = 'taskuser'
db_name = 'tasks'
db_port = 3306
engine = create_engine(f'mysql+pymysql://{db_user}:{DB_password}@{DB_URL}:{db_port}/{db_name}', echo=True)

try:
    connect = engine.connect()
    print('connect db')
    connect.close()
except Exception as e:
    print(e)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))
    password = Column(String(100))

Base.metadata.create_all(bind=engine)