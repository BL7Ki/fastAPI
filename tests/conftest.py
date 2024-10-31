# ter esse arquivo para poder organizar melhor nossas herancas de testes
import pytest
from fastapi.testclient import (
    TestClient,  # ja tem um cliente de testes dentro do fastapi
)

from fast_zero.app import app


@pytest.fixture  # guarda o resultado da funcao pra passar como parametro em outra funcao
def client():  # Dont Repeat Yourself
    return TestClient(app)


@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    table_registry.metadata.drop_all(engine)
