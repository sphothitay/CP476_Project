from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template( 'index.html' )

@app.route('/login', methods=['POST'])
def login():
	return "TODO: login user"

@app.route('/register', methods=['POST'])
def register():
	return "TODO: Register user"

@app.route('/debate')
def debate():
	return render_template( 'debate.html' )

@app.route('/topics')
def topics():
	return render_template( 'topics.html' )

@app.route('/createTopic')
def createTopic():
	return render_template( 'createTopic.html' )
