from sqlalchemy import create_engine, text
from config import settings
from model import metadata_obj

engine=create_engine(
    url=settings.DATABASE_URL,
    #echo=True,
    pool_size=5,
    max_overflow=10
)

def eng_conn():
    with engine.connect() as conn:
        res=conn.execute(text("Select VERSION()"))

def create_table():
    metadata_obj.create_all(engine)

create_table()