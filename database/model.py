from sqlalchemy import Table, Column,Integer,Boolean,String,MetaData

metadata_obj=MetaData()

sub_table=Table(
    "Абоненты",
    metadata_obj,
    Column("id",Integer,primary_key=True),
    Column("addr",String),
    Column("count_model",String),
    Column("count_num",Integer),
    Column("modem_num",Integer),
    Column("mopem_type",Boolean)

)