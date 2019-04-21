# Reddit to Instagram repost bot

## Reposts hot posts from any subreddit onto instagram

### How to use:
* Download package from github
* Install all the requirements (see below)
* Fill in your Reddit username, password, client_id, client_secret on inbot.py (line 16-19) if you don't have a client_id click [here](https://ssl.reddit.com/prefs/apps/ "Set up bot")
* Fill in the subreddit you want to post to, the amount of posts per day and the hashtags on inbot.py (line 9-11)
* Fill in your instagram username and password on instagram.js (line 1-2)
* Run by going to the directory instagrambot and typing 'python inbot.py'
* Leave Running


If you have any questions feel free to ask and fill free to add stuff as it is open source

### requirements
* praw 'pip install praw'
* PIL 'pip install Pillow'
* Naked.toolshed.shell 'pip install Naked'
* nodejs [Download here](https://nodejs.org/en/ "Download nodejs")
* [instagram-private-api](https://github.com/dilame/instagram-private-api "link to instagram-private-api") 'npm install instagram-private-api' 


### ToDo:
* Allow it to post gifs
* Some reddit posts don't work, may be due to having dots and other characters in the title
* Simplify process
