from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/membership')
def membership():
    return render_template('membership.html')


@app.errorhandler(404)
def not_found(e):
    return render_template('home.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
