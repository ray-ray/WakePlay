from flask import Flask
from flask import request


import data
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


def status_str():
    output = "<h1>Who's Awake?</h1><table><tr><th>Name</th><th>State</th></tr>"
    for user in data.users.itervalues():
        output += "<tr><td>%s</td><td>%s</td></tr>" % (user['name'], user['state'])
    output += '</table>'
    return output


@app.route('/status')
def status():
    return status_str()

@app.route('/test')
def test():
    if data.users['cMqObMnzHc8']['state'] == 'awake':
        data.users['cMqObMnzHc8']['state'] = 'asleep'
    else:
        data.users['cMqObMnzHc8']['state'] = 'awake'
    return status_str()


@app.route('/play')
def play():
    """
    Add logic here for the pandora redirects based on sleep state.
    """
    return 'Not done yet'

if __name__ == '__main__':
    app.run()
