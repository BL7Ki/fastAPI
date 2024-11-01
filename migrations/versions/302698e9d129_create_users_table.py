"""create users table

Revision ID: 302698e9d129
Revises: 
Create Date: 2024-10-31 23:19:46.569370

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '302698e9d129'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

"""
Esse arquivo descreve as mudanças a serem feitas no banco de dados. Ele usa a linguagem core do SQLAlchemy, que é mais baixo nível que o ORM. 
As funções upgrade e downgrade definem, respectivamente, o que fazer para
aplicar e para desfazer a migração. No nosso caso, a função upgrade cria a tabela 'users' com os campos que definimos em fast_zero/models.py e a função downgrade a remove.
"""
