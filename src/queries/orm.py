from database import engine, session_factory
from src.model import CountOrm,  metadata_obj






def create_table():
    metadata_obj.drop_all(engine)
    metadata_obj.create_all(engine) 

def insert_data():
    count_gub=CountOrm(
       addr="губернаторская 3",
       count_model="Merk",
       count_num=666,
       modem_num=1111111)
    with session_factory() as session:
        session.add(count_gub)
        session.commit()
  

