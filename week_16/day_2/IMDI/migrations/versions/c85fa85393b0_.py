"""empty message

Revision ID: c85fa85393b0
Revises: 3fbb395610cf
Create Date: 2020-08-09 18:38:12.162798

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c85fa85393b0'
down_revision = '3fbb395610cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('film_rating', sa.Column('rating', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('film_rating', 'rating')
    # ### end Alembic commands ###
