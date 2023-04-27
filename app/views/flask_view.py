from flask import Flask, render_template
from ..utils import file_opener


app = Flask(__name__)

@app.route('/')
def index():
    data = file_opener("players")
    report = "Tournament report"
    return render_template('index.html', data=[data, report])

class FlaskView:
    def __init__(self):
        self.app = app
        self.start_flask_app()

    def start_flask_app(self):
        self.app.run(debug=True, use_reloader=False, port=8080)
