from flask import Flask
from flask import request

echoserver = Flask(__name__)

@echoserver.route("/hello")
def hello():
    name = request.args.get('name', default="World")

    html = "<h3>Hello {name}!</h3>"
    return html.format(name = name)

if __name__ == "__main__":
    echoserver.run(host='0.0.0.0', port=80)