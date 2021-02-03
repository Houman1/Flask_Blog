from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    name = request.args.get("name", "Page")
    return f'<h1>Home, {escape(name)}!</h1>'

@app.route('/about')
def about():
    name = request.args.get("name", "Page")
    return f'<h1>About, {escape(name)}!</h1>'


if __name__ == '__main__':
    app.run(debug=True)