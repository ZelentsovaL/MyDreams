"""empty message

Revision ID: 35467208c492
Revises: a8bec3c85229
Create Date: 2025-01-31 00:26:15.591840

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '35467208c492'
down_revision: Union[str, None] = 'a8bec3c85229'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'completed_wishes', 'users_wishes', ['wish_id'], ['wish_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'completed_wishes', type_='foreignkey')
    # ### end Alembic commands ###
