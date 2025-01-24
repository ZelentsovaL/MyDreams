"""empty message

Revision ID: 59df54f47cc9
Revises: 3a4cb1e4e10b
Create Date: 2025-01-24 13:52:05.857047

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '59df54f47cc9'
down_revision: Union[str, None] = '3a4cb1e4e10b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('photo', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profiles', 'photo')
    # ### end Alembic commands ###
