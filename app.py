#!/usr/bin/env python

from flask import Flask, render_template, request, jsonify
import openai
import load_env
import os

# Load environment variables from all .env files in the current directory
load_env.load()

openai.api_key = os.environ.get('OPENAI_API_KEY')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/openai', methods=['POST'])
def openai_post():
    data = request.json
    from pprint import pprint as pp
    pp(data)
    endpoint = data["openaiEndpoint"]
    model = data["model"]
    messages = [
        {"role": data["role1"], "content": data["content1"]},
        {"role": data["role2"], "content": data["content2"]}
    ]
    
    response = getattr(openai, endpoint).create(model=model, messages=messages)
    pp(response)
    return jsonify({'output': response})

if __name__ == '__main__':
    app.run(debug=True)
