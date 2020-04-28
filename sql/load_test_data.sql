USE DebateDB;

INSERT INTO Users (Username, Password)
VALUES ('user1', '$2b$12$Oz124XzEkQnmJwtZtYtW2.eIJS4JyedMahttZ3BvpOzBtWE5JGZaK');
INSERT INTO Users (Username, Password)
VALUES ('user2', '$2b$12$Oz124XzEkQnmJwtZtYtW2.eIJS4JyedMahttZ3BvpOzBtWE5JGZaK');
INSERT INTO Users (Username, Password)
VALUES ('user3', '$2b$12$Oz124XzEkQnmJwtZtYtW2.eIJS4JyedMahttZ3BvpOzBtWE5JGZaK');
INSERT INTO Users (Username, Password)
VALUES ('user4', '$2b$12$Oz124XzEkQnmJwtZtYtW2.eIJS4JyedMahttZ3BvpOzBtWE5JGZaK');
INSERT INTO Users (Username, Password)
VALUES ('user5', '$2b$12$Oz124XzEkQnmJwtZtYtW2.eIJS4JyedMahttZ3BvpOzBtWE5JGZaK');

INSERT INTO Topics (TopicName, TopicDescription)
VALUES ('Wildlife', 'Talk about wildlife here!');
INSERT INTO Topics (TopicName, TopicDescription)
VALUES ('Politics', 'A topic for debating all kinds of politics');
INSERT INTO Topics (TopicName, TopicDescription)
VALUES ('Veganism', 'yum yum veggies');
INSERT INTO Topics (TopicName, TopicDescription)
VALUES ('Technology', '');
INSERT INTO Topics (TopicName, TopicDescription)
VALUES ('Law', '');
INSERT INTO Topics (TopicName, TopicDescription)
VALUES ('Television', '');

INSERT INTO Arguments (ArgumentTitle, ArgumentContent, User1ID, User2ID, TopicID)
VALUES ('We should embrace communism', '', 1, 2, 1);
INSERT INTO Arguments (ArgumentTitle, ArgumentContent, User1ID, User2ID, TopicID)
VALUES ('Hot dogs are not sandwiches', 'They are closed on one side its not a sandwich just a whiter taco', 2, 3, 2);
INSERT INTO Arguments (ArgumentTitle, ArgumentContent, User1ID, User2ID, TopicID)
VALUES ('Ketchup is a valid sundae topping', '', 3, 1, 4);
INSERT INTO Arguments (ArgumentTitle, ArgumentContent, User1ID, User2ID, TopicID)
VALUES ('Another Argument', 'This just shows that multiple arguments can have the same name', 3, 4, 2);
INSERT INTO Arguments (ArgumentTitle, ArgumentContent, User1ID, TopicID)
VALUES ('Opinion', 'This just shows that multiple arguments can have the same name', 1, 2);

INSERT INTO Messages (MessageContent, ArgumentID, UserID)
VALUES ('No.', 3, 1);
INSERT INTO Messages (MessageContent, ArgumentID, UserID)
VALUES ('Subs are the same, does that make them not sandwiches?', 2, 3);

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
