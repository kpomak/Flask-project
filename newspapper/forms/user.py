from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, validators


class RegistrationForm(FlaskForm):
    username = StringField("Username", [validators.DataRequired()])
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    email = StringField(
        "email",
        [validators.DataRequired(), validators.Email()],
        filters=[lambda data: data and data.lower()],
    )
    password = PasswordField(
        "Password", [validators.DataRequired(), validators.EqualTo("confirm_password")]
    )
    confirm_password = PasswordField("Confirm password", [validators.DataRequired()])
    submit = SubmitField("Register")
