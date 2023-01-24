"""empty message

Revision ID: f928e86e8d68
Revises: 22a1dd288dc0
Create Date: 2023-01-24 00:27:31.649980

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "f928e86e8d68"
down_revision = "22a1dd288dc0"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "tags",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=32), server_default="", nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "articles_tag_association",
        sa.Column("article_id", sa.Integer(), nullable=False),
        sa.Column("tag_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["article_id"],
            ["articles.id"],
        ),
        sa.ForeignKeyConstraint(
            ["tag_id"],
            ["tags.id"],
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("articles_tag_association")
    op.drop_table("tags")
    # ### end Alembic commands ###