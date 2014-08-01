from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/wakeup')
def wakeup():
    return "Here's the pubsub!"


if __name__ == '__main__':
    app.run()
