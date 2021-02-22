"""empty message

Revision ID: bcaa80df330f
Revises: 7a10e1b7ec82
Create Date: 2021-02-18 18:45:20.075949

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bcaa80df330f'
down_revision = '7a10e1b7ec82'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('past_shows_count', sa.Integer(), nullable=True))
    op.add_column('Venue', sa.Column('seeking_description', sa.String(length=500), nullable=True))
    op.add_column('Venue', sa.Column('seeking_talent', sa.Boolean(), nullable=False))
    op.add_column('Venue', sa.Column('upcoming_shows_count', sa.Integer(), nullable=True))
    op.add_column('Venue', sa.Column('website', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'website')
    op.drop_column('Venue', 'upcoming_shows_count')
    op.drop_column('Venue', 'seeking_talent')
    op.drop_column('Venue', 'seeking_description')
    op.drop_column('Venue', 'past_shows_count')
    # ### end Alembic commands ###
