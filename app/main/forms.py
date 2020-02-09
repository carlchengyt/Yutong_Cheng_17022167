from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Email


class SignupForm(FlaskForm):
    email_address = StringField('Email address', validators=[DataRequired(), Email()],
                                render_kw={"placeholder": "Enter Email"})
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')]
                             , render_kw={"placeholder": "Enter Password"})
    confirm = PasswordField('Repeat Password', render_kw={"placeholder": "Repeat Password"})
    submit = SubmitField('Sign Up')
