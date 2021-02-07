from flask import Flask, escape, request, render_template, url_for

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)