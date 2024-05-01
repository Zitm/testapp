from pydantic import BaseModel


class Sub(BaseModel):
    addr:str
    count_model:str
    count_num:int
    modem_num:int
    modem_type:bool

    def constr(ad,cm,cn,mn,mt):
        temp=Sub(addr=ad,count_model=cm,count_num=cn,modem_num=mn,modem_type=mt)
        return temp.model_dump()

a=Sub.constr("lol","olo",1,2,True)
print(a)
