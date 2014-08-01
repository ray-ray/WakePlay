from flask import Flask
from flask import request


import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/wakeup', methods=['GET', 'POST'])
def wakeup():
    if request.method == 'POST':
        payload = request.get_json()
        print payload
        return json.dumps(payload)
    else:
        return "Here's the pubsub!"


if __name__ == '__main__':
    app.run()
