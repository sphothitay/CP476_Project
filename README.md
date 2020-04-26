# CP476 Term Project

## Debate Website

### Getting Started

The site is easy to launch using [Docker](https://docs.docker.com/get-docker/)!  

Setting up and launching the site is easy, just do `docker-compose up` in the root folder of this repo.  
The script could take a few minutes to install dependencies. Once finished, the site will be available at http://localhost/home

To apply changes made to the source code, you will need to rebuild the docker image. To do this, you can do `docker-compose up --force-recreate`


### TODO List

Things we need to do to finish the site

+ ~~Hash passwords (make logging in/registering possible)~~
+ ~~Deal with sessions (so user can stay logged in across pages)~~
  + Note: [sessions are not secure](https://blog.miguelgrinberg.com/post/how-secure-is-the-flask-user-session). This is fine for our purposes, but should be kept in mind if using Flask.
+ Remove prototype data from templates, add variables that can be filled by `Flask.render_template()`
  + Additional considerations: users involved in arguments, comment section, 
+ Make pages actually functional (`create post` creates a new post in the DB, same with create topic, etc)
+ Implement live chat
  + websockets
  + Does each message get inserted to DB, cached until end of argument, etc?
  + Are arguments timed?
  + Is live chat its own feature, or is it used to implement arguments?
+ Decide on how to do user matchmaking for arguments
  + Request a user vs. random pools
  + Open arguments; submit argument premise and have board where users can choose what to argue
+ Add new tables/columns where necessary
+ Add database triggers if applicable
+ Decide on how to "archive" past arguments
  + Store archives as read-only files
  + Store archives in their own table
  + Keep archives in regular table, but add boolean column `archived`
+ Add messages for info/error
  + non-intrusive window above content at bottom of page with 'x' to close

### Stretch Goals
If all of the above goes well, we can start to work on some stretch goals

+ Simple markdown in posts and comments (embedded links, bold text)
  + Need to be careful to strip HTML/javascript
  + [markdown2html](https://pypi.org/project/markdown2html/) could be useful
+ Profanity filter
  + Load wordlist into cache, then replace bad words in post with \*\*\*\*
+ Spam filter
  + Track how often a user posts
  + Limit number of links in a post
  + Some complicated AI filter?
+ Searching posts by keyword(s)
  + Need some kind of index of posts
  + Could be implemented with [inverted index](https://en.wikipedia.org/wiki/Inverted_index)
    + Group by topic so users can search specific topics?
+ Moderation system
  + Keep file/table of moderator user IDs?
+ User tags/awards
  + Need new table in DB
+ Blocking topics
  + Need new table in DB
+ Blocking other users
  + Need new table in DB
+ Cache data left in forms (e.g. unfinished comment/post) when user leaves current page
  + At the very least have a "Are you sure you want to leave?" prompt


## Security Disclaimer

This application is a school project, and proper security measures have not been taken. To make this app secure, we would have to:

+ Use secure sessions, [Flask sessions are unsafe](https://blog.miguelgrinberg.com/post/how-secure-is-the-flask-user-session)\
+ Serve the app over HTTPS instead of HTTP
+ Deploy the app with a [proper server](https://flask.palletsprojects.com/en/1.1.x/deploying/#deployment), such as IIS or WSGI
