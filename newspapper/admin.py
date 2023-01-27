from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from newspapper import models
from newspapper.models.database import db


class CustomView(ModelView):
    pass


# Create admin with custom base template
admin = Admin(name="Blog Admin", template_mode="bootstrap3")
# Add views
admin.add_view(CustomView(models.Tag, db.session, category="Models"))
