"""Remove and recreate table

Revision ID: 37aca904f2e1
Revises: 196286697179
Create Date: 2024-01-11 12:01:38.115863

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '37aca904f2e1'
down_revision: Union[str, None] = '196286697179'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    def upgrade():
        # Удаление существующей таблицы
        op.drop_table('tasks')


def downgrade() -> None:
    pass
