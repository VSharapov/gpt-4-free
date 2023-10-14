from flask import Flask, render_template, request, jsonify
import subprocess
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script', methods=['POST'])
def run_script():
    proc = subprocess.Popen(["./venv/bin/python", "main.py"], stdout=subprocess.PIPE)
    output = proc.stdout.read().decode('utf-8')
    return jsonify({'output': output})

if __name__ == '__main__':
    app.run(debug=True)
