from flask_admin import Admin

from newspapper import models
from newspapper.models.database import db
from newspapper.views import admin as admin_view

admin = Admin(
    name="Blog Admin",
    index_view=admin_view.CustomAdminIndexView(),
    template_mode="bootstrap3",
)

admin.add_view(admin_view.TagAdminView(models.Tag, db.session, category="Models"))
admin.add_view(
    admin_view.ArticleAdminView(models.Article, db.session, category="Models")
)
admin.add_view(
    admin_view.CustomUserAdminView(models.CustomUser, db.session, category="Models")
)
admin.add_view(admin_view.CustomAdminView(models.Author, db.session, category="Models"))
