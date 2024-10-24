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

class UserDB(UserSchema): # herda tudo do UserSchema
    id: int

class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr

class UserList(BaseModel):
    users: list[UserPublic] # dentro da lista vai trazer o que foi cadastrado no public
    # os filtros vao vir depois no app