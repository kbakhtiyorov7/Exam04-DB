from .config import config
from sqlalchemy import URL,create_engine,MetaData
from sqlalchemy.orm import Session, declarative_base

DATABSE_URL = URL.create(
    drivername="postgres+psycopg2",
    username=config.DB_USER,
    password=config.DB_PASS,
    host=config.DB_HOST,
    port=config.DB_PORT,
    database=config.DB_NAME
)

engine = create_engine(DATABSE_URL)
metadate_obj = MetaData()