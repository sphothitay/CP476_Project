from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return "TODO: main page"

@app.route('/login', methods=['POST'])
def login():
	return "TODO: login page"

@app.route('/register', methods=['POST'])
def register():
	return "TODO: Register page"

