from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


MYSQL_USER = "root"
MYSQL_PASSWORD = "Dimadimadima2"
MYSQL_HOST = "localhost"
MYSQL_PORT = "3306"
MYSQL_DATABASE = "fastapi_db"

DATABASE_URL = F"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"


## Connection
engine = create_engine(DATABASE_URL)

## Session 
sessionLocal = sessionmaker(autoflush= False , autocommit = False , bind=engin )

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close() 


## Base
Base = declarative_base()
