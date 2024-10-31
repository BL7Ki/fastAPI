from sqlalchemy import create_engine, select

from fast_zero.models import User


def test_create_user():
    engine = create_engine('sqlite:///:database.db:')
    # engine = create_engine('sqlite:///database.db') n é bom testar assim pois estamos com um banco de dados fisico
    # com um banco de dados fisico o teste so passa uma vez pq depois o id 1 realmente passa a existir, entao
    # so criar um banco apenas em memoria
    # engine cria a conexao com o banco de dados q vamos utilizar
    # pode ser qualquer um, o melhor na minha opiniao é o PostgreSQL

    table_registry = metadata.create_all(engine)  # cria com os metadados que ja existem

    with Session(engine) as session:
        user = User(
            username='messi',
            email='messi@barcelona.com',
            password='messi10',
        )
        # session é o meio de campo entre nosso codigo e o db
        # uma area de transferencia entre os dois, como se fosse o github
        session.add(user)
        session.commit()
        session.refresh(user)  # so funciona esse refresh uma vez pq depois nem o email nem o username carregam pois sao unique
        session.scalar(  # retorna o registro do banco de dados em um objeto python
            select(User).where(User.email == 'messi@barcelona.com')
        )  # bom criar uma fixture para facilitar os testes de banco de dados

    assert user.id == 1
    assert user.username == 'messi'
