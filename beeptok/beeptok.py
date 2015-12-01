#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = "John Troon <http://prewired.pw>"
__github__ = "<https://github.com/johntroony>"
__purpose__ = "IRC bot using Twitter API to send notifications to Users afk"

Copyright (C) 2015  John Troon
This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Library General Public
License as published by the Free Software Foundation; either
version 2 of the License, or (at your option) any later version.
This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Library General Public License for more details.
You should have received a copy of the GNU Library General Public
License along with this library; if not, write to the
Free Software Foundation, Inc., 51 Franklin St, Fifth Floor,
Boston, MA  02110-1301, USA.
"""

import socket
import random
import tweepy
import re
import cPickle as pickle

from twitter_api import *
from settings import *

# Function to open a pickle file and select a random value from the saved list
def picks(filex, namex):
	""" Opens a pickle file with list object, then select a random value from the list & return it as object namex"""

	with open(filex, 'rb') as input:
	    darn = pickle.load(input)
	    namex = random.choice(darn)
	    return namex

# Twitter API wrapper
class TwitterWrapper:
    """ Wrapper for the Twitter API using Tweepy"""

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def update_status(self, message):
        try:
            self.api.update_status(status=message)
        except:
            print " Error: I can't tweet Status, !tweet failed.."

    def send_dm(self,user_id, message):
        try:
            self.api.send_direct_message(user=user_id, text=message)
        except:
            print "Error: DM failed bruh!"

# Main IRC Class functions

class IRCClient:
    """Main IRC Client functions and other logical analysis of the data sent on the Channels connected. """
	
    # Define Some static variables
    socket = None
    connected = False
    nickname = nickname
    channels = channels
    password = password


    def __init__(self):
        self.socket = socket.socket()
        self.socket.connect((server, port))
        self.send("NICK %s" % self.nickname)
        self.send("USER %(nick)s %(nick)s %(nick)s :%(nick)s" % {'nick':self.nickname})
        self.send("PRIVMSG nickserv :identify %s %s\r\n" % (self.nickname, self.password))
        
    #Add a list of nicks to send notifications     
	nickToCheck = ['ugali2015','john']

	# Owner of the Bot
	owner = 'theBOFH'
    
	# Add Twitter handles for nics to notify; e.g. tweetID = {'Xman':'johntroony','Twita':'twitter'}
	tweetID = {'ugali2015':'mario_esthe','Nick2':'her_twitter'}

	while True:
            buf = self.socket.recv(4096)
            lines = buf.split("\n")
            for data in lines:
                data = str(data).strip()

                if data == '':
                    continue
                print "I<", data
                
                # server ping/pong?
                if data.find('PING') != -1:
                    n = data.split(':')[1]
                    self.send('PONG :' + n)
                    if self.connected == False:
                        self.perform()
                        self.connected = True

                args = data.split(None, 3)
                if len(args) != 4:
                    continue
                ctx = {}
                ctx['sender'] = args[0][1:]
                ctx['type']   = args[1]
                ctx['target'] = args[2]
                ctx['msg']    = args[3][1:]

                sender = ctx['sender']
                sender_trim = re.compile(r"(!)")
                sendnick = sender_trim.split(sender)
                sendnick = sendnick[0]
                
            

                # whom to reply?
                target = ctx['target']
                if ctx['target'] == self.nickname:
                    target = ctx['sender'].split("!")[0]
                    
                                   
                # directed to the bot?
                if ctx['type'] == 'PRIVMSG' and (ctx['msg'].lower()[0:len(self.nickname)] == self.nickname.lower() or ctx['target'] == self.nickname):
                    
                    query = ctx['msg']

                    if ctx['target'] != self.nickname:
                        try:
                            query = query[len(self.nickname):]
                            query = query.lstrip(':,;. ')
                        except:
                            print "Error : while I'm mentioned!"
                        
                    # do something intelligent
                    print 'someone spoke to us: ', query
                    try:
                        response = picks('pkl_data/bot_responses.pkl', 'response')
                        self.say(response, target)
                    except:
                        print "Something bad rolled in under the hood! Error while responding.."
                
                # some basic commands
                if ctx['msg'] == '!help':
                    try:
                        self.say('available commands: !help, !troll, !tweet, !excuse, !fcat, !addbeep, !rmbeep, !stats', target)
                    except:
                        print "Error while helping..."

                if data.find('fuck') != -1:
                    try:
                        self.say(sendnick+", "+"Don't throw the word fuck anyhow", target)
                    except:
                        print "Error! 'Fuck notice' failed.."
                        
                if ctx['msg'] == '!troll':
                    try:
                        trolld = picks('pkl_data/bot_troll.pkl', 'troll')
                        self.say(trolld, target)
                    except:
                        print "Error! I can't troll.."
                
                # Owner of the bot can sent tweets using !tweet command
                if ctx['msg'].startswith('!tweet') and sendnick == owner:
                    try:
                        tweet_dat = ctx['msg'].strip('!tweet')
    
                        if len(tweet_dat) < 140 :
                            wrapper = TwitterWrapper(consumer_key, consumer_secret, access_token, access_token_secret)
                            wrapper.update_status(tweet_dat)
                            self.say("Tweet sent!", target)
                    except:
                        print "Error!! I can't tweet.."
                        self.say("Tweet not sent.. Try < 140 chars bruh..", target)
                
                for nick in nickToCheck:
                    # Check if Nick is mentioned and send a Twitter DM
                    if data.find(nick) != -1:
                        msg = ctx['msg'].strip(nick)
                        dmx = ": left you a message on "+target
                        tmp = sendnick+dmx
                        temp = sendnick+": "+msg+" "+target
                        tid = tweetID[nick]
                        
                        try:
                            if len(temp) < 140 :
                                wrapper = TwitterWrapper(consumer_key, consumer_secret, access_token, access_token_secret)
                                wrapper.send_dm(tid, temp )
                                self.say("beep! sent", target)
                            
                            else:                                
                                wrapper = TwitterWrapper(consumer_key, consumer_secret, access_token, access_token_secret)
                                wrapper.send_dm(tid, tmp)
                                self.say("yah beep! sent", target)
                        except:
                            print "Error: I can't Sent a DM!"

                # check if !excuse command is issued, to send a random BOFH excuse 
                if ctx['msg'] == '!excuse':
                    try:
                        excuse = picks('pkl_data/bot_excuses.pkl', 'excuses')
                        self.say(excuse, target)
                    except:
                        print "Error: I can't make Exceuses!"

                # Check if !fcat command is issued, to send a cat fact 
                if ctx['msg'] == '!fcat':
                    try:
                        fcats = picks('pkl_data/bot_fcat.pkl', 'fcat')
                        self.say(fcats, target)
                    except:
                        print "Error: Facts about Cats failed! Meow!"
                
                # Add A new User to get alerts/notifications
                if ctx['msg'].startswith('!addbeep') and sendnick == owner:
                    if ctx['msg'].find('=') != -1:
                        try:
                            newOne = ctx['msg'].strip('!addbeep')
                            newone = newOne.strip()
                            newonex = newone.split("=")                       
                            new_nick = newonex[0]
                            new_tid = newonex[1]                       
                            tweetID[new_nick] = new_tid
                            nickToCheck.append(new_nick)
                            self.say(new_nick+": added on the notification listed!", target)
                        except:
                            self.say("Can not add "+new_nick+" "+new_tid, target)
                    else:
                        self.say("use !addbeep nick=twitter_handle", target)

                    
                # Remove User from getting alerts
                if ctx['msg'].startswith('!rmbeep') and sendnick == owner:
                    try:
                        offnick = ctx['msg'].strip('!rmbeep')
                        offnickx = offnick.strip()
                        tweetID.pop(offnickx)
                        self.say(offnick+": removed from the notifications!", target)
                    except:
                        self.say(offnick+" not removed. Maybe an error/not present..", target)
                        
                # Print the current nicks set for notifications        
                if ctx['msg'] == '!stats':
                    self.say("Here are the current Nicks..", target)
                    try:
                        for userx in tweetID.keys() :
                            self.say("Nick: "+userx+ ", TwitterID: "+tweetID[userx], target)
                    except:
                        self.say("Oops! Something went wrong...", target)
                    
                 # for debugging
#                if ctx['msg'] == '!dbug':
#                    sender = ctx['sender']
#                    typex = ctx['type']
#                    target = ctx['target']
#                    msg = ctx['msg']
#                    
#                    self.say(sender, target)
#                    self.say(typex, target)
#                    self.say(target, target)
#                    self.say(msg, target)
                    

    def send(self, msg):
        print "I>",msg
        self.socket.send(msg+"\r\n")
        
    def say(self, msg, to):
        self.send("PRIVMSG %s :%s" % (to, msg))
        
    def perform(self):
        #self.send("PRIVMSG R : Register <>")
        self.send("PRIVMSG R : Login <>")
        self.send("MODE %s +x" % self.nickname)
        for c in self.channels:
            self.send("JOIN %s" % c)
            # say hello to every channel
            self.say('Wow! Feeling sexy :P', c)
    
           
# Main

main = IRCClient()

if __name__ == "__main__":
    main()
