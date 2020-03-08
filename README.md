# CP476 Term Project

## Debate Website

### Getting Started

Note: this guide assumes you are using a Windows machine, and have Python 3.0 or higher installed.  
See [here](https://flask.palletsprojects.com/en/1.1.x/cli/) for info on other platforms.

The site is easy to launch using Docker for Windows!

If you don't have docker installed, install it [here](https://hub.docker.com/editions/community/docker-ce-desktop-windows).

To launch the site, run `deploy.ps1` in Windows Powershell.
The script will take a few minutes to install dependencies, but once finished the site will be available at http://localhost:80/home

**TODO:** convert deploy.ps1 to a `docker-compose.yml` for cross-platform support.


### TODO List

Things we need to do to finish the site

+ ~~Hash passwords (make logging in/registering possible)~~
+ Deal with sessions (so user can stay logged in across pages)
+ Remove prototype data from templates, add variables that can be filled by `Flask.render_template()`
+ Make pages actually functional (`create post` creates a new post in the DB, same with create topic, etc)
+ Figure out how to implement live chat
+ Decide on how to do user matchmaking for arguments
+ Add new tables/columns where necessary
+ Add database triggers if applicable
+ Decide on how to "archive" past arguments

If all of the above goes well, we can start to work on some stretch goals

+ Simple markdown in posts and comments (embedded links, bold text)
+ Profanity filter
+ Spam filter
+ Searching posts by keyword(s)
+ Moderation system
+ User tags/awards
+ Blocking topics
+ Blocking other users
