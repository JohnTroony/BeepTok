## BeepTok - IRC Bot

Beeptok is a Python IRC Bot that makes use of Twitter API to send alerts to IRC users with a Twitter Account.
Here we've details and a guide on how to setup and mange the bot (and possibly expand on the functions).

## Dependencies
BeepTok needs Python 2.7 with the following modules installed:

- tweepy
- socket
- random
- re
- cPickle


## Setting up Beeptok bot

* Clone the repository on your computer
```bash
$ git clone https://github.com/JohnTroony/BeepTok.git BeepTok-Bot
```

* Install tweepy (if you don't have it).
```python
$ pip install tweepy
```

* Open **beeptok/settings.py** and enter the IRC Server and port to connect;
Enter Nickname and password for the Bot and the channels to connect. For example:
```python
server = 'irc.solidirc.com'
port = 6667
nickname = 'BeepBot'
channels = ['#demo']
password = 'passwd'
```

* Also get your Twitter API keys; if you don't have them, get from [apps.twitter.com](https://apps.twitter.com/) (create a new app). Open **beeptok/twitter_api.py** and fill in the values appropriately. For example:
```python
consumer_key = "xxxxxxxxxxxxxxxxxxxxx"
consumer_secret = "xxxxxxxxxxxxxXxxxxxxxxxxxxxxxxxxxxxxx"
access_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
access_token_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```
* Now open **beeptok/beeptok.py** and on class **IRCClient** look for the following variables to edit/update:
```python
# Add a list of nicks to send notifications (when afk & mentioned).   
nickToCheck = ['troon','Nick2']

# Owner of the Bot
owner = 'troon'
    
# Add Twitter handles for nicks to notify; Format {nick:twitter_handle}
tweetID = {'troon':'johntroony','Nick2':'twitter_handle'}
```

* Run the beepbot.py 
```python 
$ python beepbot.py
```

## User Commands on IRC

* `!help` - prints help message
* `!troll` - prints a troll message
* `!fcat` - prints a fact about cats
* `!excuse` - prints a BOFH excuse

## Admin commands on IRC

* `!tweet` - Sends tweet to the Twitter Timeline. E.g `!tweet Tweet from IRC :D`
* `!addbeep Nick=TwitterID` -  Add IRC user `Nick` with his/her `TwitterID` to get notifications.
* `!rmbeep Nick` -  Remove IRC `Nick` from getting notifications on Twitter when mentioned on IRC.
* `!stats` - Prints current IRC users subscribed for Twitter notification (when mentioned on IRC).

## BeepBot Notifications

IRC mention notifications are sent as DMs to a user having a Twitter account. If the user has set SMS notifications on Twitter, he/she will get the IRC notification as a SMS/Text message.

**A) If Message is too long (more than 140 characters), a predefined message is sent instead..**

![Bot notification 1](img/bot1.png)
 
First part before : shows the IRC user who mentioned you, then the predefined message followed by the IRC channel.

**B) When the message is less than 140 characters, it's sent as a DM....** 

![Bot notification 2](img/bot2.png)  

First part before : shows the IRC user who mentioned you, then the message followed by the IRC channel.

## Current Features:

- Beepbot can join multiple Chans on the same IRC server
- Beepbot can auto rejoin Chans
- Supports Private Chat (you can extend features here too!).
- Twitter notifications
- Can print cat facts, some trolls & stupid excuses
- Supports Twilio API for Text Messaging (beta)

## Contribution

To share your improvements or simply correct any mistakes committed (I like the pun): 
- Fork the repository
- Make changes
- Submit a PR with a nice commit message & easy to track changes on the code.

You can also open issues that can assist on the improvement of BeepTok.

