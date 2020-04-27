USE DebateDB;

INSERT INTO Users (Username, Password)
VALUES ('User1', 'This-Will-Be-A-Hash');
INSERT INTO Users (Username, Password)
VALUES ('User2', 'This-Will-Be-A-Hash');
INSERT INTO Users (Username, Password)
VALUES ('User3', 'This-Will-Be-A-Hash');
INSERT INTO Users (Username, Password)
VALUES ('User4', 'This-Will-Be-A-Hash');
INSERT INTO Users (Username, Password)
VALUES ('User5', 'This-Will-Be-A-Hash');

INSERT INTO Topics (TopicName, TopicDescription)
VALUES ('Wildlife', 'Talk about wildlife here!');
INSERT INTO Topics (TopicName, TopicDescription)
VALUES ('Politics', 'A topic for debating all kinds of politics');
INSERT INTO Topics (TopicName, TopicDescription)
VALUES ('Fake Topic', 'Fake Description');
INSERT INTO Topics (TopicName, TopicDescription)
VALUES ('Blank Topic', '');

INSERT INTO Arguments (ArgumentTitle, ArgumentContent, User1ID, User2ID, TopicID)
VALUES ('Argument 1', 'This is the argument body; need to figure out how to format this', 1, 2, 1);
INSERT INTO Arguments (ArgumentTitle, ArgumentContent, User1ID, User2ID, TopicID)
VALUES ('Argument 2', '', 2, 3, 2);
INSERT INTO Arguments (ArgumentTitle, ArgumentContent, User1ID, User2ID, TopicID)
VALUES ('Another Argument', 'This is the first argument with the name "Another Argument"', 3, 1, 4);
INSERT INTO Arguments (ArgumentTitle, ArgumentContent, User1ID, User2ID, TopicID)
VALUES ('Another Argument', 'This just shows that multiple arguments can have the same name', 3, 4, 2);

INSERT INTO Messages (MessageContent, ArgumentID, UserID)
VALUES ('opinion', 1, 1);
INSERT INTO Arguments (ArgumentTitle, ArgumentContent, UserID, TopicID)
VALUES ('FACTS', 1, 2);
INSERT INTO Arguments (ArgumentTitle, ArgumentContent, UserID, TopicID)
VALUES ('good point', 1, 1);
INSERT INTO Arguments (ArgumentTitle, ArgumentContent, UserID, TopicID)
VALUES ('case closed',1, 2);

INSERT INTO Comments (Content, ArgumentID, UserID)
VALUES ('Hello World :)', 1, 1);
INSERT INTO Comments (Content, ArgumentID, UserID)
VALUES ('I am a comment!', 2, 2);
INSERT INTO Comments (Content, ArgumentID, UserID, ParentComment)
VALUES ('I am a response to a comment', 3, 2, 1);

/* Post 1 should have +3, 2 gets -1, 3 gets -2, 4 gets 0 */
INSERT INTO Votes (IsUpvote, UserID, ArgumentID)
VALUES (true, 1, 1);
INSERT INTO Votes (IsUpvote, UserID, ArgumentID)
VALUES (true, 2, 1);
INSERT INTO Votes (IsUpvote, UserID, ArgumentID)
VALUES (true, 3, 1);
INSERT INTO Votes (IsUpvote, UserID, ArgumentID)
VALUES (false, 1, 2);
INSERT INTO Votes (IsUpvote, UserID, ArgumentID)
VALUES (false, 1, 3);
INSERT INTO Votes (IsUpvote, UserID, ArgumentID)
VALUES (false, 2, 3);
INSERT INTO Votes (IsUpvote, UserID, ArgumentID)
VALUES (true, 1, 4);
INSERT INTO Votes (IsUpvote, UserID, ArgumentID)
VALUES (false, 2, 4);
