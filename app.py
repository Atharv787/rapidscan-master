from flask import Flask, request, jsonify, render_template, redirect, url_for, abort
from flask_cors import CORS
from my_module import trigger_404
from my_module import contact

import sys
print(sys.path)


app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/password-reset')
def password_reset():
    return render_template('password-reset.html')

@app.route('/trigger_404')
def trigger_404():
    abort(404)  # This will invoke the 404 error handler

# 404 Error Handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/contact')
def contact_route():
    return render_template('contact.html')



@app.route('/scan', methods=['POST'])
def scan_website():
    data = request.json
    url = data.get('url')

    if url:
        result_message = f"The website '{url}' was scanned successfully."
        return jsonify({"message": result_message}), 200
    else:
        return jsonify({"message": "Invalid URL provided."}), 400

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
