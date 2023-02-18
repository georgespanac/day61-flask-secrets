from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import Label, SubmitField
from wtforms.fields import StringField

app = Flask(__name__)
app.secret_key = "some secret string"

@app.route("/")
def home():
    return render_template('index.html')


class LoginForm(FlaskForm):
    email_label = Label(field_id="email", text="Email")
    email = StringField(label='email')
    password_label = Label(field_id="password", text="Password")
    password = StringField(label='password')
    button = SubmitField()

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    return render_template('login.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True)