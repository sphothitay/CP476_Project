import sql_queries as queries
from flask import Flask
from flask import render_template, redirect, url_for, make_response
from flask import request, session
from bcrypt import checkpw as check_password
from os import urandom
import json


app = Flask(__name__)
app.secret_key = urandom(32)
app.config['SESSION_TYPE'] = 'filesystem' # TODO: Change this


def user_logged_in():
	if 'username' not in session or 'arguserinfo' not in request.cookies:
		return False
	return request.cookies['arguserinfo'] == session['username']

@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
	if user_logged_in():
		opinions = queries.GetUserArguments(session['userid'])
		arguments = queries.GetTopOpinions()
		return render_template('index.html', arguments=arguments, opinions=opinions)
	errcode = request.args.get('err')
	if errcode is not None:
		return handle_login_error(errcode)
	return render_template('login.html')

@app.route('/logout', methods=['POST'])
def logout():
	res = make_response(redirect(url_for('index')))
	res.set_cookie('arguserinfo', '', max_age=0)
	res.set_cookie('arguserid', '', max_age=0)
	if 'username' in session:
		del session['username']
	if 'userid' in session:
		del session['userid']
	return res

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
		session['userid'] = user['UserID']
		res = make_response(redirect(request.referrer or url_for('index')))
		res.set_cookie("arguserinfo", session['username'], max_age=60*60*24*7)
		res.set_cookie("arguserid", str(session['userid']), max_age=60*60*24*7)
		return res
	
	return redirect(url_for('index', err='invalid_login'))

@app.route('/post/<int:post_id>/join', methods=["POST"])
def joinArgument(post_id):
	return json.dumps( queries.OpinionToArgument( session['userid'], post_id ) )

@app.route('/post/<int:post_id>/member', methods=["POST"])
def isArgumentMember(post_id): # check if user is a member
	arg = queries.GetArgument(post_id)
	if not arg: return "false"
	return json.dumps( session['userid'] in (arg['User1ID'], arg['User2ID']) )

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

	_id = queries.CreateUser(username, password)
	if _id:
		session['username'] = username
		session['userid'] = _id
		res = make_response(redirect(url_for('index')))
		res.set_cookie('arguserinfo', username, max_age=60*60*24*7)
		res.set_cookie('arguserid', str(_id), max_age=60*60*24*7)
		return res
	return redirect(url_for('index', err='create_failed'))

# TODO: Use TopicDescription & TopicID in topics.html template
@app.route('/topics')
def topics():
	if not user_logged_in():
		return redirect(url_for('index'))
	topics = queries.GetTopics()
	return render_template('topics.html', topics=topics)

@app.route('/opinions')
def opinions():
	if not user_logged_in():
		return redirect(url_for('index'))
	opinions = queries.GetOpinions()
	return render_template('opinions.html', opinions=opinions)

@app.route('/createTopic', methods=["GET", "POST"])
def createTopic():
	if not user_logged_in():
		return redirect(url_for('index'))
	if request.method == "POST":
		if 'name' in request.form and 'description' in request.form:
			name = request.form['name']
			description = request.form['description']
			queries.CreateTopic( name, description )
		return redirect( url_for('topics') )
		# TODO: Add form validation for required inputs
	else:
		return render_template('createTopic.html')

@app.route('/createOpinion', methods=["GET", "POST"])
def createOpinion():
	if not user_logged_in():
		return redirect(url_for('index'))
	if request.method == "POST":
		if  'opinionTitle' in request.form and 'opinion' in request.form:
			title = request.form['opinionTitle']
			content = request.form['opinion']
			topicID = request.form['topicID']
			user1ID = session['userid']
			id = queries.CreateOpinion(title, content, topicID, user1ID)
		return redirect( url_for('getPost', post_id=id) )
		# TODO: Add form validation for required inputs
	else:
		return render_template('createOpinion.html')

@app.route('/post/<int:post_id>/send', methods=['POST'])
def send_message(post_id):
	# Validation here would be nice, 1000000000 things could go wrong
	argument = queries.GetArgument(post_id)
	if session['userid'] not in (argument['User1ID'], argument['User2ID']):
		return "false"
	message = request.json['text']
	return json.dumps(queries.CreateMessage(message, post_id, session['userid']))

@app.route('/post/<int:post_id>/upvote', methods=['POST'])
def upvote(post_id):
	return json.dumps(queries.UpvotePost(session['userid'], post_id))

@app.route('/post/<int:post_id>/downvote', methods=['POST'])
def downvote(post_id):
	return json.dumps(queries.DownvotePost(session['userid'], post_id))

@app.route('/post/<int:post_id>/clearvote', methods=['POST'])
def removeVote(post_id):
	return json.dumps(queries.RemoveVote(session['userid'], post_id))

@app.route('/post/<int:post_id>/<int:message_id>/getRecent', methods=['POST'])
def getRecent(post_id, message_id):
	result = queries.GetRecent(post_id, message_id)
	return json.dumps(result if result else [], default=str)

@app.route('/post/<int:post_id>')
def getPost(post_id):
	if not user_logged_in():
		return redirect(url_for('index'))
	argument = queries.GetArgument(post_id)
	return render_template('debate.html', arg=argument)

@app.route('/post/user/<int:user_id>')
def getUserPosts(user_id):
	if not user_logged_in():
		return redirect(url_for('index'))
	user = queries.GetUser(user_id)
	arguments = queries.GetUserArguments(user_id)
	opinions = queries.GetUserOpinions(user_id)
	return render_template('debate.html', opinions=opinions, arguments=arguments, Title='Posts from ' + user['Username'])

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
