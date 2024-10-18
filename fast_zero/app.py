from fastapi import FastAPI  # importa o objeto, a funcao fastapi() em si

app = FastAPI()  # instanciando um objeto
# agora o app tem a funcao da funcao fastapi()


@app.get('/')
def read_root():  # leia a raiz, pq o / é o primeiro detudo
    return {'message': 'Olá Mundo'}
