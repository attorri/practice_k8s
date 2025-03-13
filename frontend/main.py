from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return 'hello, this is the main page :) <a href="https://deepseek.com">DeepSeek</a>'

@app.route('/<name>')
def user(name):
    return 'Hello {}!'.format(name)

@app.route('/admin')
def admin():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)