from sqlalchemy import Column, ForeignKey, Integer, Table

from newspapper.models.database import db

article_tag_association_table = Table(
    "articles_tag_association",
    db.metadata,
    Column("article_id", Integer, ForeignKey("articles.id"), nullable=False),
    Column("tag_id", Integer, ForeignKey("tags.id"), nullable=False),
)
