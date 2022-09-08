"""empty message

Revision ID: ea8450521821
Revises: 0b51a9ce9126
Create Date: 2022-09-04 16:06:53.357645

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "ea8450521821"
down_revision = "0b51a9ce9126"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("products", sa.Column("is_deleted", sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("products", "is_deleted")
    # ### end Alembic commands ###
