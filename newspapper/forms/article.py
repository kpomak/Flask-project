from flask_wtf import FlaskForm
from wtforms import (SelectMultipleField, StringField, SubmitField,
                     TextAreaField, validators)


class CreateArticleForm(FlaskForm):
    title = StringField(
        "Title",
        [validators.DataRequired()],
    )

    body = TextAreaField(
        "Body",
        [validators.DataRequired()],
    )

    submit = SubmitField("Publish")

    tags = SelectMultipleField("Tags", coerce=int)
