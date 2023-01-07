"""admin creating

Revision ID: ebd4351dac08
Revises: 6572f42b4ba9
Create Date: 2023-01-05 03:53:59.475945

"""
from newspapper.models import CustomUser
from newspapper.models.database import db

# revision identifiers, used by Alembic.
revision = "ebd4351dac08"
down_revision = "6572f42b4ba9"
branch_labels = None
depends_on = None


def upgrade():

    admin = CustomUser(username="admin", password="12345", is_staff=True)
    db.session.add(admin)
    db.session.commit()


def downgrade():
    admin = CustomUser.query.filter_by(username="admin")
    db.session.delete(admin)
    db.seesion.commit()
