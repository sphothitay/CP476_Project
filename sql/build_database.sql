/* Drop old database if it exists, then create new copy to use */
DROP DATABASE IF EXISTS DebateDB;
CREATE DATABASE DebateDB;
USE DebateDB;

CREATE TABLE Topics (
	TopicName varchar(255) UNIQUE NOT NULL, /* Short, descriptive name for the topic */
	TopicDescription text NOT NULL, /* In depth description of the topic */

	TopicID int NOT NULL AUTO_INCREMENT,
	PRIMARY KEY(TopicID)
)
;

CREATE TABLE Users (
	Username varchar(255) UNIQUE NOT NULL,
	Password varchar(255) NOT NULL, /* This will be hashed/salted */

	UserID int NOT NULL AUTO_INCREMENT,
	PRIMARY KEY(UserID)
)
;

CREATE TABLE Arguments (
	ArgumentTitle varchar(512), /* Limit number of characters in title to save space */
	ArgumentContent text,
	Created timestamp DEFAULT CURRENT_TIMESTAMP,

	ArgumentID int NOT NULL AUTO_INCREMENT,
	User1ID int NOT NULL,
	User2ID int,
	TopicID int NOT NULL,
	PRIMARY KEY(ArgumentID),
	FOREIGN KEY(User1ID) REFERENCES Users(UserID) ON DELETE CASCADE,
	FOREIGN KEY(User2ID) REFERENCES Users(UserID) ON DELETE CASCADE,
	FOREIGN KEY(TopicID) REFERENCES Topics(TopicID) ON DELETE CASCADE
)
;

CREATE TABLE Messages (
	MessageContent varchar(1024),
	Created timestamp DEFAULT CURRENT_TIMESTAMP,

	MessageID int NOT NULL AUTO_INCREMENT,
	ArgumentID int NOT NULL,
	UserID int NOT NULL,
	PRIMARY KEY(MessageID),
	FOREIGN KEY(UserID) REFERENCES Users(UserID) ON DELETE CASCADE,
	FOREIGN KEY(ArgumentID) REFERENCES Arguments(ArgumentID) ON DELETE CASCADE
)
;

CREATE TABLE IF NOT EXISTS Votes (
	IsUpvote boolean NOT NULL, /* Argument gets +1 points if true, else -1 */

	UserID int NOT NULL,
	ArgumentID int NOT NULL,
	PRIMARY KEY(UserID, ArgumentID),
	FOREIGN KEY(UserID) REFERENCES Users(UserID)
		ON DELETE CASCADE,
	FOREIGN KEY(ArgumentID) REFERENCES Arguments(ArgumentID)
		ON DELETE CASCADE
)
;

CREATE TABLE Notifications (
	Message text NOT NULL, /* Actual message the notification is sending */

	NotificationID int NOT NULL AUTO_INCREMENT,
	UserID int NOT NULL, /* Which user the notification is direced at */
	ArgumentID int NOT NULL, /* Which argument the notification is for */
	PRIMARY KEY(NotificationID),
	FOREIGN KEY(UserID) REFERENCES Users(UserID)
		ON DELETE CASCADE,
	FOREIGN KEY(ArgumentID) REFERENCES Arguments(ArgumentID)
		ON DELETE CASCADE
)
;
