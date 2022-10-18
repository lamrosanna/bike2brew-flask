"""empty message

Revision ID: 56e5a71d4bad
Revises: 1951e259977c
Create Date: 2022-10-14 10:07:39.310553

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56e5a71d4bad'
down_revision = '1951e259977c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('breweries', 'state',
               existing_type=sa.VARCHAR(length=2),
               type_=sa.String(length=50),
               existing_nullable=True)
    op.alter_column('breweries', 'postal_code',
               existing_type=sa.VARCHAR(length=10),
               type_=sa.String(length=15),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('breweries', 'postal_code',
               existing_type=sa.String(length=15),
               type_=sa.VARCHAR(length=10),
               existing_nullable=True)
    op.alter_column('breweries', 'state',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=2),
               existing_nullable=True)
    # ### end Alembic commands ###
