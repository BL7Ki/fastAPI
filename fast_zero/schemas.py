from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str
    # batata: str, assim crio a chave batata e ela VAI ter que existir
    # msg Ola Mundo
    # com este contrato, a chave message SEMPRE vai existir
    # e o valor string tambem sera obrigatorio

class UserSchema(BaseModel):
    username: str
    email: EmailStr # validando melhor o email
    password: str

class UserPublic(BaseModel):
    username: str
    email: EmailStr