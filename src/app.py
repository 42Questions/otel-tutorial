import flask

from src.constants import APP_NAME
from src.telemetry.metrics import increment_counter
from src.telemetry.traces import trace
from src.utils import foo

app = flask.Flask(APP_NAME)

def run():
    app.run(host="0.0.0.0", port=5000)

@app.route("/")
@increment_counter(2)
@trace()
def hello():
    foo()
    return "Hello, World!"
