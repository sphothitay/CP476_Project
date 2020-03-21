import sql_queries as queries
from flask import Flask
from flask import render_template, redirect, url_for
from flask import request, session
from bcrypt import checkpw as check_password
from os import urandom

app = Flask(__name__)
app.secret_key = urandom(32)
app.config['SESSION_TYPE'] = 'filesystem' # TODO: Change this

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
	if 'username' in session and session['username'] is not None:
		return render_template('index.html')
	errcode = request.args.get('err')
	if errcode is not None:
		return handle_login_error(errcode)
	return render_template('login.html')

@app.route('/logout', methods=['POST'])
def logout():
	if 'username' in session:
		del session['username']
	return redirect(url_for('index'))

@app.route('/login', methods=['POST'])
def login():
	if 'username' not in request.form or 'password' not in request.form:
		return redirect(url_for('index'))
	
	username = request.form['username']
	password = request.form['password']
	user = queries.GetUserByUsername(username)
	if user is None:
		return redirect(url_for('index', err='not_found'))
	
	if check_password(password.encode('utf-8'), user['Password'].encode('utf-8')):
		session['username'] = user['Username']
		return redirect(request.referrer or url_for(''))
	
	return redirect(url_for('index', err='invalid_login'))

@app.route('/register', methods=['POST'])
def register():
	if 'username' not in request.form \
			or 'pass' not in request.form \
			or 'passrep' not in request.form:
		return redirect(url_for('index', err='missing_fields'))
	username = request.form['username']
	user = queries.GetUserByUsername(username)
	if user is not None:
		return redirect(url_for('index', err='already_exists'))

	password = request.form['pass']
	password_repeat = request.form['passrep']

	if password != password_repeat:
		return redirect(url_for('index', err='password_match'))

	if queries.CreateUser(username, password):
		session['username'] = username
		return redirect(url_for('index'))
	return redirect(url_for('index', err='create_failed'))

@app.route('/debate')
def debate():
	topic = 'penguins'
	messages = [ 
		{ 'message':'Hello World!', 'sent': False}, 
		{ 'message':'Hello to you too!', 'sent': True}
	]
	related = [
		{'href': '#test-1', 'title': 'Some other thing'},
		{'href': '#test-2', 'title': 'A related posty post'}
	]
	return render_template('debate.html', topic=topic, messages=messages, related=related )

# TODO: Use TopicDescription & TopicID in topics.html template
@app.route('/topics')
def topics():
	topics = queries.GetTopics()
	return render_template('topics.html', topics=topics)

@app.route('/createTopic', methods=["GET", "POST"])
def createTopic():
	if request.method == "POST":
		if 'name' in request.form and 'description' in request.form:
			name = request.form['name']
			description = request.form['description']
			queries.CreateTopic( name, description )
		return redirect( url_for('topics') )
	else:
		return render_template('createTopic.html')

@app.route('/post/<int:post_id>')
def getPost(post_id):
	argument = queries.GetArgument(post_id)
	# TODO: edit debate template, render template with debate contents
	return render_template('debate.html')

# TODO: finish this function, add error option for login page
def handle_login_error(errcode):
	errmsg = 'Something went wrong. Try again later.'

	if errcode == 'password_match':
		errmsg = 'Passwords do not match'
	if errcode == 'already_exists':
		errmsg = 'User already exists, choose a different username'
	if errcode == 'not_found':
		errmsg = 'User not found'
	if errcode == 'invalid_login':
		errmsg = 'Incorrect username or password'
	if errcode == 'missing_fields':
		errmsg = 'All fields must be filled to continue'
	return render_template('login.html', error=errmsg)

@app.errorhandler(404)
def page_not_found(e):
    return app.send_static_file('404.html'), 404
