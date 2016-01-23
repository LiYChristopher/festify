# http://code.runnable.com/UiPhLHanceFYAAAP/how-to-perform-ajax-in-flask-for-python

from library import app
from flask import render_template, request, jsonify


# This route will show a form to perform an AJAX request
# jQuery is loaded to execute the request and update the
# value of the operation
@app.route('/')
def index():
    return render_template('index.html')

# Route that will process the AJAX request
@app.route('/_add_numbers', methods = ['POST'])
def add_numbers():
    a = request.json['a']
    b = request.json['b']
    return jsonify(result=a + b)