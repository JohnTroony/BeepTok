# BeebTok
Python IRC Bot 

BeebTok is a simple python IRC bot that makes use of Twitter API to send alerts to IRC users with a Twitter Account.

## Commands
It has other commands you can use once you deploy, such as : 

* `!help` - prints help message
* `!troll` - prints a troll message
* `!fcat` - prints a fact about cats
* `!excuse` - prints a BOFH excuse

### Some Bot Admin commands
* `!tweet` -sends tweet to the Twitter Timeline 
* `!addbeep Nick=TwitterID` -  Add IRC user `Nick` with his/her `TwitterID` to get notifications.
* `!rmbeep Nick` -  Remove IRC `Nick` from getting notifications on Twitter when mentioned on IRC.
* `!stats` - Prints current IRC users subscribed for Twitter notification (when mentioned on IRC).

## Notifications
IRC mention notifications are sent as DMs to the IRC user having a Twitter account. If the user has set SMS notifications of Twitter the better.

- If Message is too long (> 140 characters), a predefined message is sent instead
![Bot notification 1](img/bot1.png) First part before : shows the IRC user who mentioned you, then the predefined message followed by the IRC channel.

- When the message is less than 140 characters, it's sent as a DM. 
![Bot notification 2](img/bot2.png)  First part before : shows the IRC user who mentioned you, then the message followed by the IRC channel.

"more commands to come"

## Current Support:
- Multiple Chans
- Auto Rejoin Chans

## Dependencies
BeepTok needs Python 2.7 with the following modules installed:

- tweepy
- socket
- random
- re

## To Do

- Use MVP pattern
- Support for User created plug-ins
- Add Reminder (Reminds IRC users to do something e.g. meeting)
- Add Encryption
- [user ideas and wish list here]
