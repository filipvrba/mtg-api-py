from flask import Flask, jsonify, request, render_template
from db import get_content

app = Flask(__name__)

@app.route('/api/v1/')
def api():

    query = request.args.get('query')
    content = None
    if query:
        content = get_content(query)
    else:
        content = {
            "code": "Warning",
            "message": "To find the desired outcome, please enter a '?query='."
        }
    response = jsonify(content)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route('/')
def index():
    return render_template('index.html')


def create_app():
    return app


if __name__ == "__main__":
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=8080)
    app.run()
