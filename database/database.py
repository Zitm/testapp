from sqlalchemy import create_engine, text, insert
from config import settings
from model import metadata_obj, sub_table

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
    metadata_obj.drop_all(engine)
    metadata_obj.create_all(engine)

def insert_data():
    with engine.connect() as conn:
        stmt=insert(sub_table).values(
            [
                {"addr":"Губернаторская 16","count_model":"Merk","count_num":123456789,"modem_num":33333333 }
            ]
        )
        conn.execute(stmt)
        conn.commit()

create_table()
insert_data()