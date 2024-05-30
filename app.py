from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to our flask app</h1>'

@app.route('/hello/<string:name>')
def hello(name):
    return f'<h1>Buenos Dias {name}</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)