from http import (
    HTTPStatus,  # serve pra tirar o codigo 200 ou outros pra voltar o status
    # tipo o OK
)

from fastapi.testclient import (
    TestClient,  # ja tem um cliente de testes dentro do fastapi
)

from fast_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act
    # requisitando o / pra testar ela

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert
    # garantir realmente que a mensagem ola mundo que esta retornando
