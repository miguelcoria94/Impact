"""empty message

Revision ID: ed65ef7f7d56
Revises: 6a7825a0b054
Create Date: 2021-09-14 00:48:39.679121

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed65ef7f7d56'
down_revision = '6a7825a0b054'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('post_image', sa.String(length=64), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'post_image')
    # ### end Alembic commands ###
