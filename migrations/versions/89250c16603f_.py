"""empty message

Revision ID: 89250c16603f
Revises: a46aeb256206
Create Date: 2024-03-21 19:40:51.454693

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89250c16603f'
down_revision = 'a46aeb256206'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))

    # ### end Alembic commands ###