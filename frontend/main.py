import os
import requests
from flask import Flask, redirect, url_for,jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_URL = 'https://api.openai.com/v1/chat/completions'

@app.route("/")
def home():
    return 'hello, this is the main page :) <a href="https://deepseek.com">DeepSeek</a>'

@app.route('/gpt')
def gpt_4o_mini():
    headers = {
        'Authorization': f"Bearer {OPENAI_API_KEY}",
        'Content-Type': 'application/json'
    }
    
    payload = {
        'model': 'gpt-4o-mini',
        'messages': [{'role':'user', 'content':'Hello GPT!'}],
        'temperature': 0.7
    }
    
    response = requests.post(OPENAI_API_URL, json=payload, headers= headers)
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error':response.status_code, 'reason': response.text})

@app.route('/admin')
def admin():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)