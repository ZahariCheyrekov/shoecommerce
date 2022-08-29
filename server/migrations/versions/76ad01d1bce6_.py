"""empty message

Revision ID: 76ad01d1bce6
Revises: a787d93289f1
Create Date: 2022-08-29 14:31:53.560532

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "76ad01d1bce6"
down_revision = "a787d93289f1"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("user_data", "user_id", existing_type=sa.INTEGER(), nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("user_data", "user_id", existing_type=sa.INTEGER(), nullable=True)
    # ### end Alembic commands ###
