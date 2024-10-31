from http import (
    HTTPStatus,  # serve pra tirar o codigo 200 ou outros pra voltar o status
    # tipo o OK
)


def test_root_deve_retornar_ok_e_ola_mundo(client):
    # client = TestClient(app)  # Arrange

    response = client.get('/')  # Act
    # requisitando o / pra testar ela

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert
    # garantir realmente que a mensagem ola mundo que esta retornando


def test_create_user(client):
    # client = TestClient(app) # Arrange

    response = cliente.post(
        '/users/',
        json={  # enviando o UserSchema pra testar
            'username': 'messi',
            'email': 'messi@barcelona.com',
            'password': 'messi123',
        }
    )  # act

    assert response.status_code == HTTPStatus.CREATED  # 201
    assert response.json() == {
            'username': 'messi',
            'email': 'messi@barcelona.com',
            'password': 'messi123',
            'id': 1
    }


def test_read_users(client):  # pessimo habito pq ainda n tenho banco de dados real, so o momentaneo
    # com isso, preciso rodar o post primeiro e depois esse

    response = client.get('/users/')  # act

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
            'username': 'messi',
            'email': 'messi@barcelona.com',
            'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'messi',
            'email': 'messi@barcelona.com',
            'password': 'messi123',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }  # put enviar sempre todos os dados, um especifico so o PATCH


def test_delete_user(client):
    response = client.delete('/users/1')  # pq é o unico id que tem de momento

    assert response.status_code == HTTPStatus.OK  # retorna 200 ou 204, vc que sabe
    assert response.json() == {'message': 'User deleted'}


def test_update_user_should_return_not_found(client):
    response = client.put(
        '/users/8',
        json={
            'username': 'messi',
            'email': 'messi@barcelona.com',
            'password': 'messi123',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user_should_return_not_found(client):
    response = client.delete('/users/666')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}  # validar que ele ta dando essa mensagem


def test_get_user_id_should_return_not_found(client):
    response = client.get('/users/8')  # ja coloca um que nao existe no sistema

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_get_user_id(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
            'username': 'messi',
            'email': 'messi@barcelona.com',
            'password': 'messi123',  # faz o molde pq aqui ele ta testando um que de fato existe
            # ai vc retorna o padrao do schema criado
    }
