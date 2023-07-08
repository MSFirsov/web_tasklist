"""rename date_id -> num_week_day

Revision ID: d32c69b0bd75
Revises: 67b710627e7b
Create Date: 2023-07-08 14:39:44.852834

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd32c69b0bd75'
down_revision = '67b710627e7b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('num_week_day', sa.Integer(), nullable=True))
        batch_op.drop_index('ix_task_date_id')
        batch_op.create_index(batch_op.f('ix_task_num_week_day'), ['num_week_day'], unique=False)
        batch_op.drop_column('date_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_id', sa.INTEGER(), nullable=True))
        batch_op.drop_index(batch_op.f('ix_task_num_week_day'))
        batch_op.create_index('ix_task_date_id', ['date_id'], unique=False)
        batch_op.drop_column('num_week_day')

    # ### end Alembic commands ###
