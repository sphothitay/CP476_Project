CREATE TABLE IF NOT EXISTS Topics (
	TopicName varchar(255) UNIQUE NOT NULL, /* Short, descriptive name for the topic */
	TopicDescription text NOT NULL, /* In depth description of the topic */

	TopicID int NOT NULL AUTO_INCREMENT,
	PRIMARY KEY(TopicIC)
)
;

CREATE TABLE IF NOT EXISTS Users (
	Username varchar(255) UNIQUE NOT NULL,
	Password varchar(255) NOT NULL, /* This will be hashed/salted */

	UserID int NOT NULL AUTO_INCREMENT,
	PRIMARY KEY(UserID)
)
;

CREATE TABLE IF NOT EXISTS Arguments (
	ArgumentTitle varchar(512), /* Limit number of characters in title to save space */
	ArgumentContent text,
	Created timestamp DEFAULT CURRENT_TIMESTAMP,

	ArgumentID int NOT NULL AUTO_INCREMENT,
	UserID int NOT NULL,
	TopicID int NOT NULL,
	PRIMARY KEY(ArgumentID),
	FOREIGN KEY(UserID) REFERENCES Users(UserID) ON DELETE CASCADE,
	FOREIGN KEY(TopicID) REFERENCES Topics(TopicID) ON DELETE CASCADE
)
;

CREATE TABLE IF NOT EXISTS Comments (
	Content text NOT NULL,
	ParentComment int DEFAULT NULL,

	CommentID int NOT NULL AUTO_INCREMENT,
	ArgumentID int NOT NULL,
	UserID int NOT NULL,
	PRIMARY KEY(CommentID),
	FOREIGN KEY(ArgumentID) REFERENCES Posts(ArgumentID)
		ON DELETE CASCADE,
	FOREIGN KEY(UserID) REFERENCES Users(UserID)
		ON DELETE CASCADE
)
;

CREATE TABLE IF NOT EXISTS CommentVotes (
	IsUpvote boolean NOT NULL, /* Comment gets +1 points if true, else -1 */

	UserID int NOT NULL,
	CommentID int NOT NULL,
	PRIMARY KEY(UserID, CommentID),
	FOREIGN KEY(UserID) REFERENCES Users(UserID)
		ON DELETE CASCADE,
	FOREIGN KEY(CommentID) REFERENCES Comments(CommentID)
		ON DELETE CASCADE
)
;

CREATE TABLE IF NOT EXISTS Votes (
	IsUpvote boolean NOT NULL, /* Argument gets +1 points if true, else -1 */

	UserID int NOT NULL,
	ArgumentID int NOT NULL,
	PRIMARY KEY(UserID, ArgumentID),
	FOREIGN KEY(UserID) REFERENCES Users(UserID)
		ON DELETE CASCADE,
	FOREIGN KEY(ArgumentID) REFERENCES Posts(ArgumentID)
		ON DELETE CASCADE
)
;

CREATE TABLE IF NOT EXISTS Notifications (
	Message text NOT NULL, /* Actual message the notification is sending */

	NotificationID int NOT NULL AUTO_INCREMENT,
	UserID int NOT NULL, /* Which user the notification is direced at */
	ArgumentID int NOT NULL, /* Which argument the notification is for */
	PRIMARY KEY(NotificationID),
	FOREIGN KEY(UserID) REFERENCES Users(UserID)
		ON DELETE CASCADE,
	FOREIGN KEY(ArgumentID) REFERENCES Posts(ArgumentID)
		ON DELETE CASCADE
)
;

