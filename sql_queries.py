import mysql.connector
import bcrypt
import os
from time import sleep

def CreateUser( username, password ):
	queryString = '''INSERT INTO 
Users (Username, Password) 
VALUES (%s, %s)'''
	hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
	return doInsert( queryString, (username, hashed) )

def CreateTopic(name, description):
	queryString = '''INSERT INTO 
Topics (TopicName, TopicDescription) 
VALUES (%s, %s)'''
	return doInsert( queryString, (name, description) )

def CreateArgument(Title, Content, TopicID, User1ID, User2ID):
	queryString = '''INSERT INTO 
Arguments (ArgumentTitle, ArgumentContent, TopicID, User1ID, User2ID) 
VALUES (%s, %s, %s, %s, %s)'''
	return doInsert( queryString, (Title, Content, TopicID, User1ID, User2ID) )

def CreateOpinion(Title, Content, TopicID, User1ID):
	queryString = '''INSERT INTO 
Arguments (ArgumentTitle, ArgumentContent, TopicID, User1ID) 
VALUES (%s, %s, %s, %s)'''
	return doInsert( queryString, (Title, Content, TopicID, User1ID) )

def UpvoteArgument(UserID, ArgumentID):
	queryString = '''INSERT INTO Votes (IsUpvote, UserID, ArgumentID) VALUES (true, %s, %s)
ON DUPLICATE KEY UPDATE
	IsUpvote = true
'''
	try:
		db = GetDB()
		cursor = db.cursor(buffered=True)
		cursor.execute( queryString, (UserID, ArgumentID) )
		return True # Don't use lastrowid here, in case of update
	except mysql.connector.Error:
		return False

def DownvoteArgument(UserID, ArgumentID):
	queryString = '''INSERT INTO Votes (IsUpvote, UserID, ArgumentID) VALUES (false, %s, %s)
ON DUPLICATE KEY UPDATE
	IsUpvote = false
'''
	try:
		cursor = GetDB().cursor(buffered=True)
		cursor.execute( queryString, (UserID, ArgumentID) )
		return True # Don't use lastrowid here, in case of update
	except mysql.connector.Error:
		return False

def RemoveVote(UserID, ArgumentID):
	queryString = '''DELETE FROM Votes WHERE UserID=%s AND ArgumentID=%s'''
	try:
		cursor = GetDB().cursor(buffered=True)
		cursor.execute( queryString, (UserID, ArgumentID) )
		return True
	except mysql.connector.Error:
		return False

def OpinionToArgument(user2ID, ArgumentID):
	queryString = '''UPDATE Arguments
SET User2ID = CASE
	WHEN User2ID = NULL THEN %s
	ELSE User2ID
WHERE ArgumentID = %s'''
	result = runQuery( queryString, (user2ID, ArgumentID) )
	if len(result) == 0:
		return False
	return True

def CreateMessage(MessageContent, ArgumentID, UserID):
	queryString = '''INSERT INTO 
Messages (MessageContent, ArgumentID, UserID)
VALUES (%s, %s, %s)'''
	return doInsert( queryString, (MessageContent, ArgumentID, UserID) )

def GetTopArguments():
	queryString = '''SELECT * FROM Arguments as A ORDER BY Created ASC LIMIT 20'''
	result = runQuery( queryString, tuple() )
	return result

def GetTopOpinions():
	queryString = '''SELECT * FROM Arguments AS A
	WHERE User2ID IS NULL ORDER BY Created ASC LIMIT 20'''
	result = runQuery( queryString, tuple() )
	return result

def GetArgument( argumentID ):
	queryString = '''SELECT *
FROM Arguments AS A
INNER JOIN Topics as T
ON A.TopicID=T.TopicID
WHERE ArgumentID=%s'''
	result = runQuery( queryString, (argumentID, ) )
	if len(result) == 0:
		return None
	return result[0]

def CheckSimilarTopic(argumentTitle):
	queryString = '''SELECT * FROM Topics WHERE TopicName=%s'''
	result = runQuery( queryString, (argumentTitle, ) )
	if len(result) == 0:
		return False
	return True

def GetArgumentMessages( argumentID ):
	queryString = '''SELECT * FROM Messages
WHERE ArgumentID=%s
ORDER BY Created ASC'''
	result = runQuery( queryString, (argumentID, ) )
	if len(result) == 0:
		return None
	return result

def GetOpinions():
	queryString = '''SELECT * FROM Arguments
WHERE User2ID is NULL
ORDER BY Created ASC'''
	result = runQuery( queryString, () )
	return result

def GetUserOpinions( userID ):
	queryString = '''SELECT * FROM Arguments AS A
INNER JOIN Topics as T 
ON A.TopicID=T.TopicID 
WHERE User1ID=%s AND User2ID is NULL'''
	result = runQuery( queryString, (userID, ) )
	return result

def GetRecent( argumentID, messageID ):
	queryString = '''SELECT * FROM Messages
WHERE ArgumentID=%s and MessageID > %s
ORDER BY Created ASC'''
	result = runQuery( queryString, (argumentID, messageID, ) )
	if len(result) == 0:
		return None
	return result

def GetUserArguments( userID ):
	queryString = '''SELECT * FROM Arguments AS A
INNER JOIN Topics as T 
ON A.TopicID=T.TopicID
INNER JOIN
	(SELECT ArgumentID, SUM(IF(IsUpvote, 1, -1)) as NumVotes
	FROM Votes
	GROUP BY ArgumentID) AS VQ
ON A.ArgumentID=VQ.ArgumentID
WHERE User1ID=%s OR User2ID=%s'''
	result = runQuery( queryString, (userID, userID) )
	return result

def GetTopics():
	queryString = '''SELECT * FROM Topics'''
	return runQuery( queryString, tuple() )

def SearchTopics( topicName ):
	queryString = '''SELECT * FROM Topics WHERE TopicName LIKE %s'''
	result = runQuery( queryString, (topicName, ) ) 
	if len(result) == 0:
		return None
	return result

def GetComment( commentID ):
	queryString = '''SELECT * FROM Comments WHERE CommentID=%s'''
	result = runQuery( queryString, (commentID, ) )
	if len(result) == 0:
		return None
	return result[0]

def GetUser( userID ):
	queryString = '''SELECT * FROM Users WHERE UserID=%s'''
	result = runQuery( queryString, (userID, ) )
	if len(result) == 0:
		return None
	return result[0]

def GetUserByUsername( username ):
	queryString = '''SELECT * FROM Users WHERE Username=%s'''
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
			host="localhost", user="root",
			passwd=os.environ['MYSQL_PASSWORD'],
			database="DebateDB")
		databaseConnection.autocommit = True
	return databaseConnection

def doInsert( queryString, params ):
	try:
		db = GetDB()
		while not db.is_connected(): sleep(10) # Wait until connection is free
		cursor = db.cursor(buffered=True)
		cursor.execute( queryString, params )
		cursor.close()
		_id = cursor.lastrowid
		return _id
	except mysql.connector.Error:
		return False


def runQuery( queryString, params ):
	db = GetDB()
	while not db.is_connected(): sleep(10) # Wait until connection is free
	cursor = db.cursor(buffered=True)
	cursor.execute( queryString, params )
	result = cursor.fetchall()
	columns = cursor.column_names
	cursor.close()
	
	return tuple({ columns[i]:entry[i] for i in range(len(columns)) } for entry in result)

