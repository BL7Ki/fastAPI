from http import (
    HTTPStatus,  # serve pra tirar o codigo 200 ou outros pra voltar o status
    # tipo o OK
)

def test_root_deve_retornar_ok_e_ola_mundo(client):
    #client = TestClient(app)  # Arrange

    response = client.get('/')  # Act
    # requisitando o / pra testar ela

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert
    # garantir realmente que a mensagem ola mundo que esta retornando


def test_create_user(client):
    #client = TestClient(app) # Arrange

    response = cliente.post(
        '/users/',
        json = { # enviando o UserSchema pra testar
            'username': 'testando',
            'email': 'testando@gmail.com',
            'password': 'senha123',
        }
    ) # act

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
            'username': 'testando',
            'email': 'testando@gmail.com',
            'password': 'senha123',
            'id': 1
    }