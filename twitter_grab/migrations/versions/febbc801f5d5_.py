"""empty message

Revision ID: febbc801f5d5
Revises: ce090f8b90cb
Create Date: 2018-06-28 07:54:00.943251

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'febbc801f5d5'
down_revision = 'ce090f8b90cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hashtag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('faa_twitter_id', sa.Integer(), nullable=True),
    sa.Column('hashtag', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hashtag')
    # ### end Alembic commands ###
