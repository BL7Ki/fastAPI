from pydantic import BaseModel


class Message(BaseModel):
    message: str
    # batata: str, assim crio a chave batata e ela VAI ter que existir
    # msg Ola Mundo
    # com este contrato, a chave message SEMPRE vai existir
    # e o valor string tambem sera obrigatorio