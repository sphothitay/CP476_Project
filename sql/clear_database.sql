USE DebateDB;

DELETE FROM Users;
DELETE FROM Topics;
/* The above should cascade to all other tables, 
but we will do the rest just in case */
DELETE FROM Arguments;
DELETE FROM Comments;
DELETE FROM CommentVotes;
DELETE FROM Votes;
DELETE FROM Notifications;