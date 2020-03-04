import mysql.connector


def GetArgument( argumentID ):
	queryString = '''SELECT * FROM Arguments AS A
INNER JOIN Topics as T
ON A.TopicID=T.TopicID
WHERE ArgumentID=%s'''
	result = runQuery( queryString, (argumentID, ) )
	if len(result) == 0:
		return None
	return result[0]

def GetComment( commentID ):
	queryString = 'SELECT * FROM Comments WHERE CommentID=%s'
	result = runQuery( queryString, (commentID, ) )
	if len(result) == 0:
		return None
	return result[0]

def GetUser( userID ):
	queryString = 'SELECT * FROM Users WHERE UserID=%s'
	result = runQuery( queryString, (userID, ) )
	if len(result) == 0:
		return None
	return result[0]

def GetUserByUsername( username ):
	queryString = 'SELECT * FROM Users WHERE Username=%s'
	result = runQuery( queryString, (username, ) )
	if len(result) == 0:
		return None
	return result[0]

def GetArgumentVoteCount( argumentID ):
	queryString = '''SELECT SUM( CASE WHEN IsUpvote THEN 1 ELSE -1 ) as NumVotes
FROM Votes WHERE ArgumentID=%s'''
	return runQuery( queryString, (argumentID, ) )[0]
	
def GetCommentVoteCount( commentID ):
	queryString = '''SELECT SUM( CASE WHEN IsUpvote THEN 1 ELSE -1 ) as NumVotes
FROM CommentVotes WHERE CommentID=%s'''
	return runQuery( queryString, (commentID, ) )[0]

def GetUserCommentVoteCount( userID ):
	queryString = '''SELECT SUM( CASE WHEN IsUpvote THEN 1 ELSE -1 ) as NumVotes
FROM CommentVotes WHERE UserID=%s'''
	return runQuery( queryString, (userID, ) )[0]

def GetUserArgumentVoteCount( userID ):
	queryString = '''SELECT SUM( CASE WHEN IsUpvote THEN 1 ELSE -1 ) as NumVotes
FROM Votes WHERE UserID=%s'''
	return runQuery( queryString, (userID, ) )[0]


databaseConnection = None
def GetDB():
	global databaseConnection
	if databaseConnection is None:
		databaseConnection = mysql.connector.connect(
			host="localhost", user="root", passwd="", database="DebateDB")
	return databaseConnection

def runQuery( queryString, params ):
	db = GetDB()
	cursor = db.cursor()
	cursor.execute( queryString, params )
	result = cursor.fetchall()
	cursor.close()
	return result

