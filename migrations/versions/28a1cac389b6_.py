"""empty message

Revision ID: 28a1cac389b6
Revises: 56e5a71d4bad
Create Date: 2022-10-14 11:06:27.429006

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28a1cac389b6'
down_revision = '56e5a71d4bad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('breweries', 'phone',
               existing_type=sa.INTEGER(),
               type_=sa.BigInteger(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('breweries', 'phone',
               existing_type=sa.BigInteger(),
               type_=sa.INTEGER(),
               existing_nullable=True)
    # ### end Alembic commands ###