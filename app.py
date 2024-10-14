from flask import Flask, request, jsonify, render_template, redirect, url_for, abort
from flask_cors import CORS
import subprocess

# Initialize Flask app with CORS
app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

# In-memory store for scan results
scan_results = {}

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
    abort(404)  # Invokes the 404 error handler

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

    if not url:
        return jsonify({"message": "URL not provided"}), 400

    try:
        # Run your scan script or logic
        command = f"python webscan.py {url}"  # Use 'python' instead of 'python3' for Windows
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Store the result in memory
        scan_results[url] = result.stdout

        # Redirect to the result page
        return redirect(url_for('scan_result', url=url))

    except Exception as e:
        return jsonify({"message": str(e)}), 500

@app.route('/result')
def scan_result():
    url = request.args.get('url')

    # Retrieve the scan result from memory
    result = scan_results.get(url, "No result found for this URL.")

    return render_template('output.html', url=url, result=result)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
