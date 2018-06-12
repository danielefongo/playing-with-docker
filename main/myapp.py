from flask import Flask
from flask import request
import db_queries

echoserver = Flask(__name__)

@echoserver.route("/hello")
def hello():
    name = request.args.get('name', default="World")

    html = "<h3>Hello {name}!</h3>"
    return html.format(name = name)

@echoserver.route("/query")
def query():
    connection = db_queries.getConnection()
    values = db_queries.doSelect(connection)

    print(generate_html_list(values))
    return generate_html_list(values)

def generate_html_list(values):
    html = ""
    for value in values:
        html += str(value) + "<br>"
    return html

@echoserver.route("/insert")
def insert():
    name = request.args.get('name')
    surname = request.args.get('surname')

    connection = db_queries.getConnection()
    values = db_queries.doInsert(connection, name, surname)

    html = "<h3>{name} {surname} added.</h3>"
    return html.format(name = name, surname = surname)

if __name__ == "__main__":
    echoserver.run(host='0.0.0.0', port=80)