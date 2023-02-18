from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import Label, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email, Length
app = Flask(__name__)
app.secret_key = "some secret string"

@app.route("/")
def home():
    return render_template('index.html')


class LoginForm(FlaskForm):

    email_label = Label(field_id="email", text="Email")
    email = EmailField(label='email', validators=[DataRequired(), Email()])
    password_label = Label(field_id="password", text="Password")
    password = PasswordField (label='password', validators=[DataRequired(), Length(min=8)])
    button = SubmitField("Log in")

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    login_form.validate_on_submit()
    return render_template('login.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True)