# aqui fica os modelos do banco de dados
# schema é o esqueleto de algo, as regras. models ja vem mais dos modelos de relacionameto
from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()  # registra os metadados


@table_registry.mapped_as_dataclass  # criando classe de dados
# uma classe sem metodos, apenas atributos, apenas dados
# é mapeada, vai mapear os tipos dos dados igual a democratizacao com c#
class User:
    __tablename__ = 'users'  # nome da tabela

    id: Mapped[int] = mapped_column(init=False, primary_key=True)  # nao inicia o id pq no futuro se tiver 50k a gente n se preocupa com isso, o db resolve
    username: Mapped[str] = mapped_column(unique=True)  # mapeando os tipos
    email: Mapped[str] = mapped_column(unique=True)  # assim n tera varias contas com o mesmo email
    password: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(init=False, server_default=func.now())  # quando foi criado ou quando foi alterado, gerar tipo um log
    # func_now() o banco de dados vai fazer e se virar nao importa o local, assim n precisamos informar a hora sempre

    """
    forma implicita e talvez mais rapida, pq um ali mapeia o tipo e o outro como a coluna deve ser

    id = mapped_column(Integer, primary_key=True)
    nome = mapped_column(String(50), nullable=False)
    idade = mapped_column(Integer)
    """
