from wtforms import Form, StringField, validators


class UserForm(Form):
    firs_name = StringField("First Name")
    last_name = StringField("Last Name")
    email = StringField("email", [validators.DataRequired(), validators.Email()])
