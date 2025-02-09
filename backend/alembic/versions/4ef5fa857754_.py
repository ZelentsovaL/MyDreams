"""empty message

Revision ID: 4ef5fa857754
Revises: 0102233fc0ba
Create Date: 2025-02-01 23:27:23.370127

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4ef5fa857754'
down_revision: Union[str, None] = '0102233fc0ba'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('completed_wishes', sa.Column('wish_title', sa.String(), nullable=False))
    op.add_column('completed_wishes', sa.Column('wish_price', sa.Float(), nullable=False))
    op.add_column('completed_wishes', sa.Column('wish_source_url', sa.String(), nullable=False))
    op.add_column('completed_wishes', sa.Column('wish_photo', sa.String(), nullable=False))
    op.drop_constraint('completed_wishes_wish_id_fkey', 'completed_wishes', type_='foreignkey')
    op.drop_column('completed_wishes', 'wish_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('completed_wishes', sa.Column('wish_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('completed_wishes_wish_id_fkey', 'completed_wishes', 'users_wishes', ['wish_id'], ['wish_id'])
    op.drop_column('completed_wishes', 'wish_photo')
    op.drop_column('completed_wishes', 'wish_source_url')
    op.drop_column('completed_wishes', 'wish_price')
    op.drop_column('completed_wishes', 'wish_title')
    # ### end Alembic commands ###
