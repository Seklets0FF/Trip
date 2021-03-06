"""empty message

Revision ID: 5618bbe5f335
Revises: cd7d4d130336
Create Date: 2020-07-25 16:26:58.825546

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5618bbe5f335'
down_revision = 'cd7d4d130336'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('name', sa.String(length=64), nullable=True))
    op.add_column('user', sa.Column('password_hash', sa.String(length=128), nullable=True))
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_name'), 'user', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_name'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_column('user', 'password_hash')
    op.drop_column('user', 'name')
    # ### end Alembic commands ###
