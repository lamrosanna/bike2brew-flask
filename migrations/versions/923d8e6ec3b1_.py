"""empty message

Revision ID: 923d8e6ec3b1
Revises: 5bd240d5a576
Create Date: 2022-10-16 21:02:13.468748

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '923d8e6ec3b1'
down_revision = '5bd240d5a576'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('favorite_breweries', 'flagged')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('favorite_breweries', sa.Column('flagged', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
