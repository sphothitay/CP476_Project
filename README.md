# CP476 Term Project

## Debate Website

### Getting Started

Note: this guide assumes you are using a Windows machine, and have Python 3.0 or higher installed.  
See [here](https://flask.palletsprojects.com/en/1.1.x/cli/) for info on other platforms.

The site is easy to launch using [Docker](https://docs.docker.com/)!  

Setting up and launching the site is easy, just do `docker-compose up -d` in the root folder of this repo.  
The script could take a few minutes to install dependencies. Once finished, the site will be available at http://localhost:80/home


### TODO List

Things we need to do to finish the site

+ ~~Hash passwords (make logging in/registering possible)~~
+ ~~Deal with sessions (so user can stay logged in across pages)~~
  + More work can probably be done on sessions, but for now it is good
+ Remove prototype data from templates, add variables that can be filled by `Flask.render_template()`
+ Make pages actually functional (`create post` creates a new post in the DB, same with create topic, etc)
+ Figure out how to implement live chat
  + websockets
+ Decide on how to do user matchmaking for arguments
+ Add new tables/columns where necessary
+ Add database triggers if applicable
+ Decide on how to "archive" past arguments
  + Store archives as read-only files
  + Store archives in their own table
  + Keep archives in regular table, but add boolean column `archived`
+ Add messages for info/error
  + non-intrusive window above content at bottom of page with 'x' to close

If all of the above goes well, we can start to work on some stretch goals

+ Simple markdown in posts and comments (embedded links, bold text)
+ Profanity filter
+ Spam filter
+ Searching posts by keyword(s)
+ Moderation system
+ User tags/awards
+ Blocking topics
+ Blocking other users
+ Cache data left in forms (e.g. unfinished comment/post) when user leaves current page
  + At the very least have a "Are you sure you want to leave?" prompt
