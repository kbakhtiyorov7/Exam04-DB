from sqlalchemy import URL, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from .config import config

DATABASE_URL = URL.create(
    drivername='postgresql+psycopg2',
    host=config.DB_HOST,
    port=config.DB_PORT,
    username=config.DB_USER,
    password=config.DB_PASS,
    database=config.DB_NAME
)
engine = create_engine(url=DATABASE_URL)
Base = declarative_base()
LocalSession = sessionmaker(engine)

def get_db():
    return LocalSession()