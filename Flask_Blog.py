from flask import Flask, escape, request, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "756fcb446d673b4bd20d82da45cf17ca"


posts = [

    {"author": "Houman Houshidar",
     "title": "arm wrestling pro question",
     "content": "how do I become a pro arm wrestler?",
     "date_posted": "03/02/2021"},
    {"author": "Cyrus Houshidar",
     "title": "response - arm wrestling pro question",
     "content": "hard work and skill",
     "date_posted": "05/02/2021"}
]


@app.route('/')
@app.route('/home')
def home():

    return render_template('home.html', posts=posts)

@app.route('/about')
def about():

    return render_template('about.html', title="about")

@app.route('/register')
def registration():
    form = RegistrationForm()
    return render_template("register.html", title="Register", form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template("Login.html", title="Login", form=form)


if __name__ == '__main__':
    app.run(debug=True)