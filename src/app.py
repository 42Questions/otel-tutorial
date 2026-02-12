import flask

from src.constants import APP_NAME
from src.telemetry.metrics import increment_counter

app = flask.Flask(APP_NAME)

def run():
    app.run(host="0.0.0.0", port=5000)

@app.route("/")
@increment_counter(2)
def hello():
    return "Hello, World!"
