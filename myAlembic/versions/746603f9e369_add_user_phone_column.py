"""Add user phone column

Revision ID: 746603f9e369
Revises: 99754ce5b84e
Create Date: 2023-04-10 16:10:25.027803

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "746603f9e369"
down_revision = "99754ce5b84e"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("user", sa.Column("phone", sa.String(length=16), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("user", "phone")
    # ### end Alembic commands ###
