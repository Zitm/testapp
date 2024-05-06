from sqlalchemy import Table, Column,Integer,Boolean,String,MetaData
from sqlalchemy.orm import Mapped,mapped_column
from src.database import Base



class CountOrm(Base):
    __tablename__="Абоненты"

    id: Mapped[int]=mapped_column(primary_key=True)
    addr:Mapped[str]
    count_model:Mapped[str]
    count_num:Mapped[int]
    modem_num:Mapped[int]








metadata_obj=MetaData()

""" sub_table=Table(
    "Абоненты",
    metadata_obj,
    Column("id",Integer,primary_key=True),
    Column("addr",String),
    Column("count_model",String),
    Column("count_num",Integer),
    Column("modem_num",Integer),
    Column("modem_type",Boolean)

)   """