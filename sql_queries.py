import mysql.connector

databaseConnection = None

def GetDB():
	global databaseConnection
	if databaseConnection is None:
		databaseConnection = mysql.connector.connect(
			host="localhost", user="root", passwd="", database="DebateDB")
	return databaseConnection

def GetArgument( db, argumentID ):
	queryString = '''SELECT * FROM Arguments AS A
INNER JOIN Topics as T
ON A.TopicID=T.TopicID
WHERE ArgumentID=%s'''
	return runQuery( db, queryString, (argumentID, ) )

def GetComment( db, commentID ):
	queryString = 'SELECT * FROM Comments WHERE CommentID=%s'
	return runQuery( db, queryString, (commentID, ) )

def GetUser( db, userID ):
	queryString = 'SELECT * FROM Users WHERE UserID=%s'
	return runQuery( db, queryString, (userID, ) )

def GetUserByUsername( db, username ):
	queryString = 'SELECT * FROM Users WHERE Username=%s'
	return runQuery( db, queryString, (username, ) )

def GetArgumentVoteCount( db, argumentID ):
	queryString = '''SELECT SUM( CASE WHEN IsUpvote THEN 1 ELSE -1 ) as NumVotes
FROM Votes WHERE ArgumentID=%s'''
	return runQuery( db, queryString, (argumentID, ) )
	
def GetCommentVoteCount( db, commentID ):
	queryString = '''SELECT SUM( CASE WHEN IsUpvote THEN 1 ELSE -1 ) as NumVotes
FROM CommentVotes WHERE CommentID=%s'''
	return runQuery( db, queryString, (commentID, ) )

def GetUserCommentVoteCount( db, userID ):
	queryString = '''SELECT SUM( CASE WHEN IsUpvote THEN 1 ELSE -1 ) as NumVotes
FROM CommentVotes WHERE UserID=%s'''
	return runQuery( db, queryString, (userID, ) )

def GetUserArgumentVoteCount( db, userID ):
	queryString = '''SELECT SUM( CASE WHEN IsUpvote THEN 1 ELSE -1 ) as NumVotes
FROM Votes WHERE UserID=%s'''
	return runQuery( db, queryString, (userID, ) )

def runQuery( db, queryString, params ):
	cursor = db.cursor()
	cursor.execute( queryString, params )
	result = cursor.fetchall()
	cursor.close()
	return result
