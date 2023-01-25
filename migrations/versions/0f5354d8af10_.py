"""empty message

Revision ID: 0f5354d8af10
Revises: ce3407bf1e4c
Create Date: 2023-01-16 05:07:44.811043

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "0f5354d8af10"
down_revision = "ce3407bf1e4c"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("custom_user", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column("first_name", sa.String(length=120), nullable=True)
        )
        batch_op.add_column(
            sa.Column("last_name", sa.String(length=120), nullable=True)
        )
        batch_op.add_column(sa.Column("email", sa.String(length=255), nullable=False))
        batch_op.create_unique_constraint(None, ["email"])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("custom_user", schema=None) as batch_op:
        batch_op.drop_constraint(None, type_="unique")
        batch_op.drop_column("email")
        batch_op.drop_column("last_name")
        batch_op.drop_column("first_name")

    # ### end Alembic commands ###