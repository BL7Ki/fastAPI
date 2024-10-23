from http import HTTPStatus
from fastapi import FastAPI  # importa o objeto, a funcao fastapi() em si
from fast_zero.schemas import (
    Message, UserSchema, UserPublic, UserDB
)
app = FastAPI()  # instanciando um objeto
# agora o app tem a funcao da funcao fastapi()

database = [] # banco de dados falso momentaneo

@app.get('/', status_code=HTTPStatus.OK, response_model=Message) # documentando
# colocando ali o que DEVE retornar
def read_root():  # leia a raiz, pq o / é o primeiro detudo
    return {'message': 'Olá Mundo'} 
# 'batata': 'frita' caso eu queira criar essa chave valor
# precisando firmar no contrato que a chave batata deve existir lá

@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic) # tipo de resposta como userPublic para ocultar a senha
# response_model=UserSchema isso arruma a doc da api pois lá no try out n volta so 'string' como resposta
def create_user(user: UserSchema): # a chave user com o valor do schema ja
    user_with_id = UserDB(**user.model_dump(), # transformar os itens do contrato em dict e desempacotar com **
                   id=len(database) + 1) # incrementando a lista

    database.append(user_with_id) # adicionando na lista

    return user_with_id
# por mais que a chave user pegue o valor userschema, o meu modelo de resposta ta como userpublic, essa é a magia
# fica status_code=HTTPStatus.CREATED pq post é sempre 201 que retorna e por padrao o fastapi vai sempre retornar 200
# por isso se for status diferente, sempre bom alterar pra n ficar tudo 200