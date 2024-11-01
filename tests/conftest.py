# ter esse arquivo para poder organizar melhor nossas herancas de testes
import pytest
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from fast_zero.models import table_registry
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

    with Session(engine) as session: # with gerencia recursos
        yield session # vai rodar ate essa linha e desfazer tudo q foi feito

    table_registry.metadata.drop_all(engine) # aqui ele deleta tudo pra recomecar o banco de dados
