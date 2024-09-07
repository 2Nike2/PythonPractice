"""Flaskの動作確認."""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Display a 'Hello, World!' message.

    This function handles the root URL ("/") of the web application and
    returns a simple "Hello, World!" message as a string response.

    Returns:
        str: The message "Hello, World!".
    """
    return "Hello, World!"
