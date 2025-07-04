"""empty message

Revision ID: b771e1b9f668
Revises: 3a87d62a3765
Create Date: 2025-06-21 15:13:50.803341

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b771e1b9f668'
down_revision: Union[str, None] = '3a87d62a3765'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recomendation_wishes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('photo', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('source_url', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('wishes_lists', sa.Column('description', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('wishes_lists', 'description')
    op.drop_table('recomendation_wishes')
    # ### end Alembic commands ###
