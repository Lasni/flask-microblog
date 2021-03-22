"""add language to posts

Revision ID: 64a2f4cb1c1b
Revises: 3e5535fd319c
Create Date: 2021-03-19 10:33:27.734897

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64a2f4cb1c1b'
down_revision = '3e5535fd319c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###