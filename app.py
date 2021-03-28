from flask import Flask
from flask import request
from flask import jsonify
from flask import Response
from backend import graphAPI

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify(
        "Welcome to LAOx, a tool for finding sources required to gain a background understanding"
        + " of topics covered in complex papers.")


@app.route("/graph", methods=['GET'])
def graph():
    body = request.json

    if not body:
        return Response(" { 'Result' : 'Error, No Json Body Given' } ",
                        status=400,
                        mimetype='application/json')

    if 'input' not in body or 'valid' not in body:
        return Response(
            " { 'Result' : 'Error, Json Body must contain paper input and valid input' } ",
            status=400,
            mimetype='application/json')

    payload, status = graphAPI.createDependencyGraph(body)

    if status == 0:
        return jsonify(payload)
    elif status == 1:
        return Response(" { 'Result' : 'Error, Invalid scraper received' } ",
                        status=400,
                        mimetype='application/json')
    elif status == 2:
        return Response(" { 'Result' : 'Error parsing link' } ",
                        status=400,
                        mimetype='application/json')
    elif status == 3:
        return Response(" { 'Result' : 'Error, non arxiv link received' } ",
                        status=400,
                        mimetype='application/json')
    elif status == 4:
        return Response(" { 'Result' : 'Error, server connection error' } ",
                        status=400,
                        mimetype='application/json')
    elif status == 5:
        return Response(
            " { 'Result' : 'Error, unknown error in graph creation' } ",
            status=400,
            mimetype='application/json')
    else:
        return Response(" { 'Result' : 'Unknown Error' } ",
                        status=400,
                        mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True)
