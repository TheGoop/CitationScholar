from flask import Flask
from flask import request
from flask import jsonify
from flask import json
from flask import Response

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify("Hello World!")


@app.route("/graph", methods=['GET'])
def graph():
    args = request.args
    body = request.json

    if not body:
        return Response(" { 'Result' : 'Error, No Json Body Given' } ", status=400, mimetype='application/json')

    dag, status = None, 0  # scraper.get_dag() or something

    if status == 0:
        return Response("Here is DAG", status=200, mimetype="application/json")
    else:
        # handle status errors
        raise NotImplementedError


if __name__ == '__main__':
    app.run(debug=True)
