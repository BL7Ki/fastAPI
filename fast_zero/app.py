from http import HTTPStatus
from fastapi import FastAPI  # importa o objeto, a funcao fastapi() em si
from fast_zero.schemas import Message

app = FastAPI()  # instanciando um objeto
# agora o app tem a funcao da funcao fastapi()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message) # documentando
# colocando ali o que DEVE retornar
def read_root():  # leia a raiz, pq o / é o primeiro detudo
    return {'message': 'Olá Mundo'} 
# 'batata': 'frita' caso eu queira criar essa chave valor
# precisando firmar no contrato que a chave batata deve existir lá