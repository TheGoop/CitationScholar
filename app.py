from flask import Flask
from flask import request
from flask import jsonify
from flask import Response
from backend import graphAPI

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify("Welcome to LAOx, a tool for finding sources required to gain a background understanding" +
                   " of topics covered in complex papers.")


@app.route("/graph", methods=['GET'])
def graph():
    body = request.json

    if not body:
        return Response(" { 'Result' : 'Error, No Json Body Given' } ", status=400, mimetype='application/json')

    if 'input' not in body:
        return Response(" { 'Result' : 'Error, Json Body must contain paper input' } ", status=400, mimetype='application/json')

    payload, status = graphAPI.createDependencyGraph(body), 0

    if status == 0:
        return jsonify(payload)
    else:
        # handle status errors
        raise NotImplementedError


if __name__ == '__main__':
    app.run(debug=True)
