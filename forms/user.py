from wtforms import Form, StringField


class UserForm(Form):
    firs_name = StringField("First Name")
