"""Update blog and user relationship

Revision ID: 2adcdb159094
Revises: 182d68c6bf0e
Create Date: 2023-04-10 22:13:22.181327

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "2adcdb159094"
down_revision = "182d68c6bf0e"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("blog", sa.Column("user_id", sa.Integer(), nullable=True))
    op.create_foreign_key(None, "blog", "user", ["user_id"], ["id"])
    op.drop_constraint("user_blog_id_fkey", "user", type_="foreignkey")
    op.drop_column("user", "blog_id")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "user", sa.Column("blog_id", sa.INTEGER(), autoincrement=False, nullable=True)
    )
    op.create_foreign_key("user_blog_id_fkey", "user", "blog", ["blog_id"], ["id"])
    op.drop_constraint(None, "blog", type_="foreignkey")
    op.drop_column("blog", "user_id")
    # ### end Alembic commands ###
