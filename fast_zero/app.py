from http import HTTPStatus

from fastapi import FastAPI  # importa o objeto, a funcao fastapi() em si

from fast_zero.schemas import Message, UserDB, UserList, UserPublic, UserSchema

app = FastAPI()  # instanciando um objeto
# agora o app tem a funcao da funcao fastapi()

database = []  # banco de dados falso momentaneo


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)  # documentando
# colocando ali o que DEVE retornar
def read_root():  # leia a raiz, pq o / é o primeiro detudo
    return {'message': 'Olá Mundo'}
# 'batata': 'frita' caso eu queira criar essa chave valor
# precisando firmar no contrato que a chave batata deve existir lá


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)  # tipo de resposta como userPublic para ocultar a senha
# response_model=UserSchema isso arruma a doc da api pois lá no try out n volta so 'string' como resposta
def create_user(user: UserSchema):  # a chave user com o valor do schema ja
    user_with_id = UserDB(**user.model_dump(),  # transformar os itens do contrato em dict e desempacotar com **
                   id=len(database) + 1)  # incrementando a lista

    database.append(user_with_id)  # adicionando na lista

    return user_with_id
# por mais que a chave user pegue o valor userschema, o meu modelo de resposta ta como userpublic, essa é a magia
# fica status_code=HTTPStatus.CREATED pq post é sempre 201 que retorna e por padrao o fastapi vai sempre retornar 200
# por isso se for status diferente, sempre bom alterar pra n ficar tudo 200


@app.get('/users/', response_model=UserList)  # na mesma url mas muda sua funcao de acordo com os verbos
def read_users():
    return {'users': database}  # guardar no nosso banco


@app.put('/users/{user_id}', response_model=UserPublic)  # userid ta dentro do link
def update_user(user_id: int, user: UserSchema):  # valor vai ser validado como um inteiro
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'  # se eu tentar alterar um id que nao existe ainda
        )

    user_with_id = UserDB(**user.model_dump(), id=user_id)  # incrementando lista
    database[user_id - 1] = user_with_id  # substituindo a posicao na lista

    return user_with_id


@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:  # mesma logica de n deletar o que nao existe
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    del database[user_id - 1]

    return {'message': 'User deleted'}


@app.get('/users/{user_id}', response_model=UserPublic)
def read_user_id(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    return database[user_id - 1]
