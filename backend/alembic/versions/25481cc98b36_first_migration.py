"""First migration

Revision ID: 25481cc98b36
Revises: 
Create Date: 2021-10-25 22:30:11.569227

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25481cc98b36'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('date_added', sa.DateTime(), nullable=True),
    sa.Column('date_updated', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_account_id'), 'account', ['id'], unique=False)
    op.create_table('mysql_query',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('sql_query', sa.Text(), nullable=True),
    sa.Column('date_added', sa.DateTime(), nullable=True),
    sa.Column('date_updated', sa.DateTime(), nullable=True),
    sa.Column('account_id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['account.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_mysql_query_id'), 'mysql_query', ['id'], unique=False)
    op.create_table('server',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('operating_system', sa.Text(), nullable=True),
    sa.Column('ip', sa.Text(), nullable=True),
    sa.Column('status', sa.Text(), nullable=True),
    sa.Column('date_added', sa.DateTime(), nullable=True),
    sa.Column('date_updated', sa.DateTime(), nullable=True),
    sa.Column('owner_account_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['owner_account_id'], ['account.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_server_id'), 'server', ['id'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('email', sa.Text(), nullable=False),
    sa.Column('first_name', sa.Text(), nullable=False),
    sa.Column('last_name', sa.Text(), nullable=False),
    sa.Column('hashed_password', sa.Text(), nullable=False),
    sa.Column('disabled', sa.Boolean(), nullable=True),
    sa.Column('date_added', sa.DateTime(), nullable=True),
    sa.Column('date_updated', sa.DateTime(), nullable=True),
    sa.Column('account_id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['account.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_server_id'), table_name='server')
    op.drop_table('server')
    op.drop_index(op.f('ix_mysql_query_id'), table_name='mysql_query')
    op.drop_table('mysql_query')
    op.drop_index(op.f('ix_account_id'), table_name='account')
    op.drop_table('account')
    # ### end Alembic commands ###
