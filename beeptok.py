 #!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
@file:beeptok.py

@author: John Troon

@purpose: IRC bot to send Twitter DM (as notifications) when a nick user is away from Keyboard.

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

# Twitter API tokens

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""


# List of Phrases for the Bot to use.
responses = ['Signs Point To Yes','Yes','You May Rely On It','Ask Again Later','Concentrate And Ask Again','My Goodness!','My Sources Say No','Better Not Tell You Now','Without A Doubt','Reply Hazy, Try Again','It Is Decidedly So','Cannot Predict Now','My Reply Is No','As I See It Yes','It Is Certain','Yes Definitely','Don\'t Count On It','Most Likely','Very Doubtful','Feeling = Not So Good']
troll = ["I can see your point, but I still think you're full of $h+t.", "I don't know what your problem is, but I'll bet it's hard to pronounce.", "How about never? Is never good for you?", "I see you've set aside this special time to humiliate yourself in public.", "I'm really easy to get along with once you learn to see it my way.", "Who lit the fuse on your tampon?", "I'm out of my mind, but feel free to leave a message.", "I don't work here. I'm a consultant.", "It sounds like English, but I can't understand a word you're saying.", "Ahhhh. I see the ****-up fairy has visited us again.", "I like you. You remind me of myself when I was young and stupid.", "You are validating my inherent mistrust of strangers.", "I have plenty of talent and vision; I just don't give a ****.", "I'm already visualizing the duct tape over your mouth.", "I will always cherish the initial misconceptions I had about you.", "Thank you. We're all refreshed and challenged by your unique point of view.", "The fact that no one understands you doesn't mean you're an artist.", "Any resemblance between your reality and mine are purely coincidental.", "What am I? Flypaper for freaks?!", "I'm not being rude. You're just insignificant.", "It's a thankless job, but I've got a lot of Karma to burn off.", "Yes, I am an agent of Satan, but my duties are largely ceremonial.", "And your cry-baby whiny-arsed opinion would be?", "Do I look like a people person to you?", "This isn't an office. It's Hell with fluorescent lighting.", "I started out with nothing and I still have most of it left.", "+++Runing Sarcasm as a service - sarcasmd started.", "If I throw a stick, will you leave?", "Errors have been made. Others will be blamed.", "Whatever kind of look you were aiming for, you missed.", "Oh I get it. Like humour, but different.........", "An office is just a mental institute without the padded walls.", "Can I swap this job for what's behind door..........1?", "Too many freaks, not enough circuses.", "Nice perfume (or aftershave). Must you marinate in it?", "Chaos, panic, and disorder. My work here is done.", "How do I set a laser printer to stun?", "I thought I wanted a career; it turns out I just needed the money.", "I'll try being nicer if you'll try being more intelligent.", "Wait a minute - I'm trying to imagine you with a personality.", "Aren't you a black hole of need.", "I'd like to help you out, which way did you come in?", "Did you eat an extra bowl of stupid this morning?", "Why don't you slip into something more comfortable? Like a coma.", "If you have something to say raise your hand... then place it over your mouth.", "I'm too busy, can I ignore you some other time?", "Don't let your mind wander, it's too small to be let out on its own.", "Have a nice day, somewhere else.", "You're not yourself today, I noticed the improvement straight away.", "Do you hear that? That's the sound of no-one caring.", "If I had a dog that looked like you, I'd shave it's butt and teach it to walk backwards.", "Do you take Karate? I was wondering because you are kicking. ", "Is that your head or did your neck vomit?", "You're so nasty, I called you on the phone and got an ear infection.", "huh?", "People like you don't grow on trees, they swing from them.", "I could say nice things about you, but I would rather tell the truth.", "I never forget a face but in your case I'll make an exception.", "I know I'm talking like an idiot. I have to, other wise you wouldn't understand me.", "Most of us live and learn, you just live.", "I like you. People say I've no taste, but I like you.", "I like your approach, now let's see your departure.", "I can't seem to remember you real name, and please don't remind me!", "can't talk to you right now; tell me, where will you be in ten years, I'll make sure I'm not there.", "You must have a low opinion of people if you think they're your equals.", "You must have gotten up on the wrong side of the cage this morning.", "You possess a mind not merely twisted, but actually sprained.", "You remind me of the ocean - you make me sick.", "You should do some soul-searching. Maybe you'll find one.", "You should have been born in the Dark Ages; you look terrible in the light.", "You should toss out more of your funny remarks; that's all they're good for.", "You started at the bottom - and it's been downhill ever since.", "You used to be arrogant and obnoxious. Now you are just the opposite. You are", "obnoxious and arrogant."]
excuses = ["clock speed", "solar flares", "electromagnetic radiation from satellite debris", "static from nylon underwear", "static from plastic slide rules", "global warming", "poor power conditioning", "static buildup", "doppler effect", "hardware stress fractures", "magnetic interference from money/credit cards", "dry joints on cable plug", "we're waiting for [the phone company] to fix that line", "sounds like a Windows problem, try calling Microsoft support", "temporary routing anomoly", "somebody was calculating pi on the server", "fat electrons in the lines", "excess surge protection", "floating point processor overflow", "divide-by-zero error", "POSIX compliance problem", "monitor resolution too high", "improperly oriented keyboard", "network packets travelling uphill (use a carrier pigeon)", "Decreasing electron flux", "first Saturday after first full moon in Winter", "radiosity depletion", "CPU radiator broken", "It works the way the Wang did, what's the problem", "positron router malfunction", "cellular telephone interference", "techtonic stress", "pizeo-electric interference", "(l)user error", "working as designed", "dynamic software linking table corrupted", "heavy gravity fluctuation, move computer to floor rapidly", "secretary plugged hairdryer into UPS", "terrorist activities", "not enough memory, go get system upgrade", "interrupt configuration error", "spaghetti cable cause packet failure", "boss forgot system password", "bank holiday - system operating credits  not recharged", "virus attack, luser responsible", "waste water tank overflowed onto computer", "Complete Transient Lockout", "bad ether in the cables", "Bogon emissions", "Change in Earth's rotational speed", "Cosmic ray particles crashed through the hard disk platter", "Smell from unhygienic janitorial staff wrecked the tape heads", "Little hamster in running wheel had coronary; waiting for replacement to be Fedexed from Wyoming", "Evil dogs hypnotized the night shift", "Plumber mistook routing panel for decorative wall fixture", "Electricians made popcorn in the power supply", "Groundskeepers stole the root password", "high pressure system failure", "failed trials, system needs redesigned", "system has been recalled", "not approved by the FCC", "need to wrap system in aluminum foil to fix problem", "not properly grounded, please bury computer", "CPU needs recalibration", "system needs to be rebooted", "bit bucket overflow", "descramble code needed from software company", "only available on a need to know basis", "knot in cables caused data stream to become twisted and kinked", "nesting roaches shorted out the ether cable", "The file system is full of it", "Satan did it", "Daemons did it", "You're out of memory", "There isn't any problem", "Unoptimized hard drive", "Typo in the code", "Yes, yes, its called a design limitation", "Look, buddy:  Windows 3.1 IS A General Protection Fault.", "That's a great computer you have there; have you considered how it would work as a BSD machine?", "Please excuse me, I have to circuit an AC line through my head to get this database working.", "Yeah, yo mama dresses you funny and you need a mouse to delete files.", "Support staff hung over, send aspirin and come back LATER.", "Someone is standing on the ethernet cable, causing a kink in the cable", "Windows 95 undocumented 'feature'", "Runt packets", "Password is too complex to decrypt", "Boss' kid fucked up the machine", "Electromagnetic energy loss", "Budget cuts", "Mouse chewed through power cable", "Stale file handle (next time use Tupperware(tm)!)", "Feature not yet implemented", "Internet outage", "Pentium FDIV bug", "Vendor no longer supports the product", "Small animal kamikaze attack on power supplies", "The vendor put the bug there.", "SIMM crosstalk.", "IRQ dropout", "Collapsed Backbone", "Power company testing new voltage spike (creation) equipment", "operators on strike due to broken coffee machine", "backup tape overwritten with copy of system manager's favourite CD", "UPS interrupted the server's power", "The electrician didn't know what the yellow cable was so he yanked the ethernet out.", "The keyboard isn't plugged in", "The air conditioning water supply pipe ruptured over the machine room", "The electricity substation in the car park blew up.", "The rolling stones concert down the road caused a brown out", "The salesman drove over the CPU board.", "The monitor is plugged into the serial port", "Root nameservers are out of sync", "electro-magnetic pulses from French above ground nuke testing.", "your keyboard's space bar is generating spurious keycodes.", "the real ttys became pseudo ttys and vice-versa.", "the printer thinks its a router.", "the router thinks its a printer.", "evil hackers from Serbia.", "we just switched to FDDI.", "halon system went off and killed the operators.", "because Bill Gates is a Jehovah witness and so nothing can work on St. Swithin's day.", "user to computer ratio too high.", "user to computer ration too low.", "we just switched to Sprint.", "it has Intel Inside", "Sticky bits on disk.", "Power Company having EMP problems with their reactor", "The ring needs another token", "new management", "telnet: Unable to connect to remote host: Connection refused", "SCSI Chain overterminated", "It's not plugged in.", "because of network lag due to too many people playing deathmatch", "You put the disk in upside down.", "Daemons loose in system.", "User was distributing pornography on server; system seized by FBI.", "BNC (brain not  (user brain not connected)", "UBNC (user brain not connected)", "LBNC (luser brain not connected)", "disks spinning backwards - toggle the hemisphere jumper.", "new guy cross-connected phone lines with ac power bus.", "had to use hammer to free stuck disk drive heads.", "Too few computrons available.", "Flat tire on station wagon with tapes.  ('Never underestimate the bandwidth of a station wagon full of tapes hurling down the highway' Andrew S. Tanenbaum) ", "Communications satellite used by the military for star wars.", "Party-bug in the Aloha protocol.", "Insert coin for new game", "Dew on the telephone lines.", "Arcserve crashed the server again.", "Some one needed the powerstrip, so they pulled the switch plug.", "My pony-tail hit the on/off switch on the power strip.", "Big to little endian conversion error", "You can tune a file system, but you can't tune a fish (from most tunefs man pages)", "Dumb terminal", "Zombie processes haunting the computer", "Incorrect time syncronization", "Defunct processes", "Stubborn processes", "non-redundant fan failure ", "monitor VLF leakage", "bugs in the RAID", "no 'any' key on keyboard", "root rot", "Backbone Scoliosis", "/pub/lunch", "excessive collisions & not enough packet ambulances", "le0: no carrier: transceiver cable problem?", "broadcast packets on wrong frequency", "popper unable to process jumbo kernel", "NOTICE: alloc: /dev/null: filesystem full", "pseudo-user on a pseudo-terminal", "Recursive traversal of loopback mount points", "Backbone adjustment", "OS swapped to disk", "vapors from evaporating sticky-note adhesives", "sticktion", "short leg on process table", "multicasts on broken packets", "ether leak", "Atilla the Hub", "endothermal recalibration", "filesystem not big enough for Jumbo Kernel Patch", "loop found in loop in redundant loopback", "system consumed all the paper for paging", "permission denied", "Reformatting Page. Wait...", "..disk or the processor is on fire.", "SCSI's too wide.", "Proprietary Information.", "Just type 'mv * /dev/null'.", "runaway cat on system.", "Did you pay the new Support Fee?", "We only support a 1200 bps connection.", "We only support a 28000 bps connection.", "Me no internet, only janitor, me just wax floors.", "I'm sorry a PC won't do, you need an SGI to connect with us.", "Post-it Note Sludge leaked into the monitor.", "the curls in your keyboard cord are losing electricity.", "The monitor needs another box of pixels.", "RPC_PMAP_FAILURE", "kernel panic: write-only-memory (/dev/wom0) capacity exceeded.", "Write-only-memory subsystem too slow for this machine. Contact your local dealer.", "Just pick up the phone and give modem connect sounds. 'Well you said we should get more lines so we don't have voice lines.'", "Quantum dynamics are affecting the transistors", "Police are examining all internet packets in the search for a narco-net-traficer", "We are currently trying a new concept of using a live mouse.  Unfortunately, one has yet to survive being hooked up to the computer.....please bear with us.", "Your mail is being routed through Germany ... and they're censoring us.", "Only people with names beginning with 'A' are getting mail this week (a la Microsoft)", "We didn't pay the Internet bill and it's been cut off.", "Lightning strikes.", "Of course it doesn't work. We've performed a software upgrade.", "Change your language to Finnish.", "Fluorescent lights are generating negative ions. If turning them off doesn't work, take them out and put tin foil on the ends.", "High nuclear activity in your area.", "What office are you in? Oh, that one.  Did you know that your building was built over the universities first nuclear research site? And wow, are'nt you the lucky one, your office is right over where the core is buried!", "The MGs ran out of gas.", "The UPS doesn't have a battery backup.", "Recursivity.  Call back if it happens again.", "Someone thought The Big Red Button was a light switch.", "The mainframe needs to rest.  It's getting old, you know.", "I'm not sure.  Try calling the Internet's head office -- it's in the book.", "The lines are all busy (busied out, that is -- why let them in to begin with?).", "Jan  9 16:41:27 huber su: 'su root' succeeded for .... on /dev/pts/1", "It's those computer people in X {city of world}.  They keep stuffing things up.", "A star wars satellite accidentally blew up the WAN.", "Fatal error right in front of screen", "That function is not currently supported, but Bill Gates assures us it will be featured in the next upgrade.", "wrong polarity of neutron flow", "Lusers learning curve appears to be fractal", "We had to turn off that service to comply with the CDA Bill.", "Ionisation from the air-conditioning", "TCP/IP UDP alarm threshold is set too low.", "Someone is broadcasting pigmy packets and the router dosn't know how to deal with them.", "The new frame relay network hasn't bedded down the software loop transmitter yet. ", "Fanout dropping voltage too much, try cutting some of those little traces", "Plate voltage too low on demodulator tube", "You did wha... oh _dear_....", "CPU needs bearings repacked", "Too many little pins on CPU confusing it, bend back and forth until 10-20% are neatly removed. Do _not_ leave metal bits visible!", "_Rosin_ core solder? But...", "Software uses US measurements, but the OS is in metric...", "The computer fletely, mouse and all.", "Your cat tried to eat the mouse.", "The Borg tried to assimilate your system. Resistance is futile.", "It must have been the lightning storm we had (yesterday) (last week) (last month)", "Due to Federal Budget problems we have been forced to cut back on the number of users able to access the system at one time. (namely none allowed....)", "Too much radiation coming from the soil.", "Unfortunately we have run out of bits/bytes/whatever. Don't worry, the next supply will be coming next week.", "Program load too heavy for processor to lift.", "Processes running slowly due to weak power supply", "Our ISP is having {switching,routing,SMDS,frame relay} problems", "We've run out of licenses", "Interference from lunar radiation", "Standing room only on the bus.", "You need to install an RTFM interface.", "That would be because the software doesn't work.", "That's easy to fix, but I can't be bothered.", "Someone's tie is caught in the printer, and if anything else gets printed, he'll be in it too.", "We're upgrading /dev/null", "The Usenet news is out of date", "Our POP server was kidnapped by a weasel.", "It's stuck in the Web.", "Your modem doesn't speak English.", "The mouse escaped.", "All of the packets are empty.", "The UPS is on strike.", "Neutrino overload on the nameserver", "Melting hard drives", "Someone has messed up the kernel pointers", "The kernel license has expired", "Netscape has crashed", "The cord jumped over and hit the power switch.", "It was OK before you touched it.", "Bit rot", "U.S. Postal Service", "Your Flux Capacitor has gone bad.", "The Dilithium Crystals need to be rotated.", "The static electricity routing is acting up...", "Traceroute says that there is a routing problem in the backbone.  It's not our problem.", "The co-locator cannot verify the frame-relay gateway to the ISDN server.", "High altitude condensation from U.S.A.F prototype aircraft has contaminated the primary subnet mask. Turn off your computer for 9 days to avoid damaging it.", "Lawn mower blade in your fan need sharpening", "Electrons on a bender", "Telecommunications is upgrading. ", "Telecommunications is downgrading.", "Telecommunications is down-shifting.", "Hard drive sleeping. Let it wake up on it's own...", "Interference between the keyboard and the chair.", "The CPU has shifted, and become decentralized.", "Due to the CDA, we no longer have a root account.", "We ran out of dial tone and we're and waiting for the phone company to deliver another bottle.", "You must've hit the wrong anykey.", "PCMCIA slave driver", "The Token fell out of the ring. Call us when you find it.", "The hardware bus needs a new token.", "Too many interrupts", "Not enough interrupts", "The data on your hard drive is out of balance.", "Digital Manipulator exceeding velocity parameters", "appears to be a Slow/Narrow SCSI-0 Interface problem", "microelectronic Riemannian curved-space fault in write-only file system", "fractal radiation jamming the backbone", "routing problems on the neural net", "IRQ-problems with the UN-Interruptible-Power-Supply", "CPU-angle has to be adjusted because of vibrations coming from the nearby road", "emissions from GSM-phones", "CD-ROM server needs recalibration", "firewall needs cooling", "asynchronous inode failure", "transient bus protocol violation", "incompatible bit-registration operators", "your process is not ISO 9000 compliant", "You need to upgrade your VESA local bus to a MasterCard local bus.", "The recent proliferation of Nuclear Testing", "Elves on strike. (Why do they call EMAG Elf Magic)", "Internet exceeded Luser level, please wait until a luser logs off before attempting to log back on.", "Your EMAIL is now being delivered by the USPS.", "Your computer hasn't been returning all the bits it gets from the Internet.", "You've been infected by the Telescoping Hubble virus.", "Scheduled global CPU outage", "Your computer has a heating problem - try cooling it with ice cold water.", "Your processor has processed too many instructions.  Turn it off immediately.", "Your packets were eaten by the terminator", "Your processor does not develop enough heat.", "We need a licensed electrician to replace the light bulbs in the computer room.", "The POP server is out of Coke", "Fiber optics caused gas main leak", "Server depressed, needs Prozak", "quantum decoherence", "those damn raccoons!", "suboptimal routing experience", "A plumber is needed, the network drain is clogged", "50% of the manual is in .pdf readme files", "the AA battery in the wallclock sends magnetic interference", "the xy axis in the trackball is coordinated with the summer solstice", "the butane lighter causes the pin-cushioning", "old inkjet cartridges emanate barium-based fumes", "manager in the cable duct", "Well fix that in the next (upgrade, update, patch release, service pack).", "HTTPD Error 666 : BOFH was here", "HTTPD Error 4004 : very old Intel cpu - insufficient processing power", "The ATM board has run out of 10 pound notes.  We are having a whip round to refill it, care to contribute ?", "Network failure -  call NBC", "Having to manually track the satellite.", "Your/our computer(s) had suffered a memory leak, and we are waiting for them to be topped up.", "The rubber band broke", "We're on Token Ring, and it looks like the token got loose.", "Stray Alpha Particles from memory packaging caused Hard Memory Error on Server.", "paradigm shift...without a clutch", "PEBKAC (Problem Exists Between Keyboard And Chair)", "The cables are not the same length.", "Second-sytem effect.", "Chewing gum on /dev/sd3c", "Boredom in the Kernel.", "the daemons! the daemons! the terrible daemons!", "I'd love to help you -- it's just that the Boss won't let me near the computer. ", "struck by the Good Times virus", "YOU HAVE AN I/O ERROR -> Incompetent Operator error", "Your parity check is overdrawn and you're out of cache.", "Communist revolutionaries taking over the server room and demanding all the computers in the building or they shoot the sysadmin. Poor misguided fools.", "Plasma conduit breach", "Out of cards on drive D:", "Sand fleas eating the Internet cables", "parallel processors running perpendicular today", "ATM cell has no roaming feature turned on, notebooks can't connect", "Webmasters kidnapped by evil cult.", "Failure to adjust for daylight savings time.", "Virus transmitted from computer to sysadmins.", "Virus due to computers having unsafe sex.", "Incorrectly configured static routes on the core-routers.", "Forced to support NT servers; sysadmins quit.", "Suspicious pointer corrupted virtual machine", "Its the InterNIC's fault.", "Root name servers corrupted.", "Budget cuts forced us to sell all the power cords for the servers.", "Someone hooked the twisted pair wires into the answering machine.", "Operators killed by year 2000 bug bite.", "We've picked COBOL as the language of choice.", "Operators killed when huge stack of backup tapes fell over.", "Robotic tape changer mistook operator's tie for a backup tape.", "Someone was smoking in the computer room and set off the halon systems.", "Your processor has taken a ride to Heaven's Gate on the UFO behind Hale-Bopp's comet.", "t's an ID-10-T error", "Dyslexics retyping hosts file on servers", "The Internet is being scanned for viruses.", "Your computer's union contract is set to expire at midnight.", "Bad user karma.", "/dev/clue was linked to /dev/null", "Increased sunspot activity.", "We already sent around a notice about that.", "It's union rules. There's nothing we can do about it. Sorry.", "Interference from the Van Allen Belt.", "Jupiter is aligned with Mars.", "Redundant ACLs. ", "Mail server hit by UniSpammer.", "T-1's congested due to porn traffic to the news server.", "Data for intranet got routed through the extranet and landed on the internet.", "We are a 100% Microsoft Shop.", "We are Microsoft.  What you are experiencing is not a problem; it is an undocumented feature.", "Sales staff sold a product we don't offer.", "Secretary sent chain letter to all 5000 employees.", "Sysadmin didn't hear pager go off due to loud music from bar-room speakers.", "Sysadmin accidentally destroyed pager with a large hammer.", "Sysadmins unavailable because they are in a meeting talking about why they are unavailable so much.", "Bad cafeteria food landed all the sysadmins in the hospital.", "Route flapping at the NAP.", "Computers under water due to SYN flooding.", "The vulcan-death-grip ping has been applied.", "Electrical conduits in machine room are melting.", "Traffic jam on the Information Superhighway.", "Radial Telemetry Infiltration", "Cow-tippers tipped a cow onto the server.", "tachyon emissions overloading the system", "Maintenance window broken", "We're out of slots on the server", "Computer room being moved.  Our systems are down for the weekend.", "Sysadmins busy fighting SPAM.", "Repeated reboots of the system failed to solve problem", "Feature was not beta tested", "Domain controller not responding", "Someone else stole your IP address, call the Internet detectives!", "It's not RFC-822 compliant.", "operation failed because: there is no message for this error (#1014)", "stop bit received", "internet is needed to catch the etherbunny", "network down, IP packets delivered via UPS", "Firmware update in the coffee machine", "Temporal anomaly", "Mouse has out-of-cheese-error", "Borg implants are failing", "Borg nanites have infested the server", "error: one bad user found in front of screen", "Please state the nature of the technical emergency", "Internet shut down due to maintenance", "Daemon escaped from pentagram", "crop circles in the corn shell", "sticky bit has come loose", "Hot Java has gone cold", "Cache miss - please take better aim next time", "Hash table has woodworm", "Trojan horse ran out of hay", "Zombie processes detected, machine is haunted.", "overflow error in /dev/null", "Browser's cookie is corrupted -- someone's been nibbling on it.", "Mailer-daemon is busy burning your message in hell.", "According to Microsoft, it's by design", "vi needs to be upgraded to vii", "greenpeace free'd the mallocs", "Terorists crashed an airplane into the server room, have to remove /bin/laden. (rm -rf /bin/laden)", "astropneumatic oscillations in the water-cooling", "Somebody ran the operating system through a spelling checker.", "Rhythmic variations in the voltage reaching the power supply.", "Keyboard Actuator Failure. Order and Replace."]
fcat = ["The heaviest cat ever recorded was 46 lbs.", "A new contender for the world's heaviest cat. Five year old Katy, who lives in Russia reportedly weighs 20kg (44 lbs). Guinness Book of Records is no longer accepting nominations in this category as they don't want to encourage pet owners to overfeed their animals.", "A tabby named 'Dusty' gave birth to 420 documented kittens in her lifetime,", "A female tabby named 'Ma' lived for 34 years, making her the oldest reliably documented housecat.", "the oldest cat still living is a Burmese called Kataleena Lady who lives in Melbourne, Australia. Kataleena Lady was born on March 11th, 1977.", "There are two cats commonly listed at the longest living. The first is Puss, who was born in 1903 and passed away on 29th November, 1939. The second is Grandpa who lived to the ripe old age of 34. was a Sphyx adopted from the Humane Society in Texas.", "A five year old moggy from Ontario, Canada is in the Guinness Book of Records for having a total of 27 toes.", "On 7th August, 1970, a four year old Burmese gave birth to 19 kittens. 15 survived 1 female & 14 males)", "A cat named Andy, holds the world record for the longest non fatal fall. Andy fell from the 16th floor (200 feet) of an apartment building.", "A cat was discovered alive in a collapsed building 80 days after an earthquake in Taiwan in December 1999.", "Jack & Donna Wright of Kingston, Ontario made their way to the Guinness Book of Records for having 689 cats.", "The world's best mouser was tortoiseshell moggy Towser. From April 21st, 1963 to 20th March 1987 she caught 28,899 mice, plus numerous other unfortunate creatures such as rats & rabbits. Towser worked for the Glenturret Distillery. A statue has been erected in the distillery grounds to honour Towser.", "A female cat named Mincho in Argentina, went up a tree and didn't come down again until she died six years later. While treed, she managed to have three litters.", "The richest cat in the Guinness Book of World Records is a pair of cats who inherited $415,000 in the early '60s. The richest single cat is a white alley cat who inherited $250,000.", "The tiniest cat on record was Tinker Toy from Illinois. A male Himalayan-Persian, he weighed 1 pound, 8 ounces fully grown and was 7.25' long and 2.75' tall! ", "Cats can't taste sweets.", "The cat's front paw has 5 toes, but the back paws have 4. Some cats are born with as many as 7 front toes and extra back toes (polydactl).", "A cat has 32 muscles in each ear.", "Neutering a cat extends it's life span by two or three years", "A cat's tongue consists of small 'hooks,' which come in handy when tearing up food", "Cats must have fat in their diet because they can't produce it on their own.", "Cat's urine glows under a black light.", "Cats have a third eyelid called a haw and you will probably only see it when kitty isn't feeling well.", "A cat sees about six times better than a human at night because of a layer of extra reflecting cells which absorb light.", "Cats sleep 16 to 18 hours per day", "Cats are the only animal that walk on their claws, not the pads of their feet.", "Newborn kittens have closed ear canals that don't begin to open for nine days.", "A kittens eyes are always blue at first", "A cat cannot see directly under its nose.", "It is a common belief that cats are color blind. However, recent studies have shown that cats can see blue, green and red", "Cats with white fur and skin on their ears are very prone to sunburn.", "Siamese kittens are born white.", "A cat's jaws cannot move sideways.", "Cats have over one hundred vocal sounds, while dogs only have about ten.", "A cat can jump even seven times as high as it is tall.", "A cat is pregnant for about 58-65 days.", "A cat may have three to seven kittens every four months", "Cats step with both left legs, then both right legs when they walk or run. The only other animals to do this are the giraffe and the camel", "If a male cat is both orange and black it is most likely sterile", "The color of the points in Siamese cats is heat related. Cool areas are darker", "Cats lack a true collarbone. Because of this, a cat can generally squeeze their bodies through any space they can get their heads through.", "There are tiny, parasitic worms that can live in a cat's stomach. These worms cause frequent vomiting.", "A cat's brain is more similar to a man's brain than that of a dog.", "A cat has more bones than a human; humans have 206, the cat has 230.", "Cats have 30 vertebrae--5 more than humans have.", "Cat have 500 skeletal muscles (humans have 650).", "A cat can rotate its ears independently 180 degrees, and can turn in the direction of sound 10 times faster than those of the best watchdog", "Cats' hearing is much more sensitive than humans and dogs.", "Cats' hearing stops at 65 khz (kilohertz); humans' hearing stops at 20 khz.", "In relation to their body size, cats have the largest eyes of any mammal.", "A cat's field of vision is about 185 degrees.", "Blue-eyed, white cats are often deaf.", "A cat has a total of 24 whiskers, 4 rows of whiskers on each side. The upper two rows can move independently of the bottom two rows", "Cats have 30 teeth (12 incisors, 10 premolars, 4 canines, and 4 molars).", "Kittens have baby teeth, which are replaced by permanent teeth around the age of 7 months.", "Cats purr at the same frequency as an idling diesel engine, about 26 cycles per second.", "The typical male housecat will weigh between 7 and 9 pounds, slightly less for female housecats.", "Cats take between 20-40 breaths per minute.", "Normal body temperature for a cat is 102 degrees F.", "A cat's normal pulse is 140-240 beats per minute, with an average of 195.", "Cats lose almost as much fluid in the saliva while grooming themselves as they do through urination", "Almost 10% of a cat's bones are in its tail.", "the tail is used to maintain balance.", "The domestic cat is the only species able to hold its tail vertically while walking.", "Female felines are 'superfecund,' which means that each of the kittens in her litter can have a different father.", "Cat saliva contains a detergent that keeps their fur clean.", "Cats have AB blood groups just like people", "Cats eyes don't glow in the dark; they only reflect light.", "Like birds, cats have a homing ability that uses its biological clock, the angle of the sun, and the Earth's magnetic field. A cat taken far from its home can return to it.", "Cats can't taste sweets.", "Cats born without tails genetically have a shorter spine and longer rear legs than other cats.", "Cats eat grass to keep their digestive systems clean. The regurgitation brings up hair and other irritants.", "Multi-colored male cats are very rare. For every 3,000 tortoiseshell or calico cats born, only one will be male", "Cats are able to hear sounds that move faster than 45,000 hertz. They could hear the sound of a bat.", "There are approximately 60,000 hairs per square inch on the back of a cat and about 120,000 per square inch on its underside", "Cats only sweat from the pads of their paws; ever notice how wet the examination room table gets when you take your cat to the vet?", "The largest cat breed is the Ragdoll. Males weigh 12-20 pounds, with females weighing 10-15 pounds.", "The smallest cat breed is the Singapura. Males weigh about 6 pounds while females weigh about 4 pounds.", "Cats don't see 'detail' very well. To them, their person may appear hazy when standing in front of them.", "Cats can see up to 120 feet away.", "Kittens begin dreaming at just over one week old.", "If an overweight cat's 'sides' stick out further than her whiskers, she will lose her sense of perception and stability. Don't be surprised if she starts to squeeze into an opening that the rest of her can't fit into", "Every cat's nose pad is unique, and no two nose prints are the same. ", "In 1987, cats overtook dogs as the number one pet in America.", "About 37% of American homes today have at least 1 cat.", "It has been scientifically proven that stroking a cat can lower one's blood pressure", "Americans spend more annually on cat food than on baby food.", "In Asia and England, black cats are considered lucky.", "The way you treat kittens in the early stages of it's life will render it's personality traits later in life.", "Tylenol and chocolate are both poisionous to cats.", "People who are allergic to cats are actually allergic to cat saliva or to cat dander. If the resident cat is bathed regularly the allergic people tolerate it better", "The chlorine in fresh tap water irritates sensitive parts of the cat's nose. Let tap water sit for 24 hours before giving it to a cat.", "The catnip plant contains an oil called hepetalactone which does for cats what marijuana does to some people.", "Not every cat gets 'high' from catnip. If the cat doesn't have a specific gene, it won't react (about 20% do not have the gene).", "Catnip is non-addictive.", "When well treated, a cat can live twenty or more years.", "allergic people should tolerate spayed female cats the best", "Cats are subject to gum disease and to dental caries. They should have their teeth cleaned by the vet or the cat dentist once a year", "Many cats cannot properly digest cow's milk. Milk and milk products give them diarrhea", "Cats can get tapeworms from eating mice. If your cat catches a mouse it is best to take the prize away from it.", "If a cat is frightened, the hair stands up fairly evenly all over the body; when the cat threatens or is ready to attack, the hair stands up only in a narrow band along the spine and tail", "Cats respond most readily to names that end in an 'ee' sound", "The female cat reaches sexual maturity within 6 to 10 months; most veterinarians suggest spaying the female at 5 months", "The male cat usually reaches sexual maturity between 9 and 12 months.", "A heat period lasts about 4 to 7 days if the female is bred; if not, the heat period lasts longer and recurs at regular intervals.", "If a cat is frightened, put your hand over its eyes and forehead, or let him bury his head in your armpit to help calm him", "A cat will tremble or shiver when it is in extreme pain.", "Neutering a male cat will, in almost all cases, stop him from spraying, fighting with other males, lengthen his life and improve its quality", "Declawing a cat is the same as cutting a human's fingers off at the knuckle.", "The average lifespan of an outdoor-only cat (feral and non-feral) is about 3 years", "Cats with long, lean bodies are more likely to be outgoing, and more protective and vocal than those with a stocky build.", "A steady diet of dog food may cause blindness in your cat - it lacks taurine.", "An estimated 50% of today's cat owners never take their cats to a veterinarian for health care.", "Most cats adore sardines.", "Cats respond better to women than to men, probably due to the fact that women's voices have a higher pitch", "According to a Gallup poll, most American pet owners obtain their cats by adopting strays.", "When your cats rubs up against you, she is actually marking you as 'hers' with her scent.", "Someone who is allergic to one cat may not be allergic to another cat. Though there isn't currently a way of predicting which cat is more likely to cause allergic reactions,", "Cat bites are more likely to become infected than dog bites - but human bites are the most dangerous of all", "Cat families usually play best in even numbers. Cats and kittens should be acquired in pairs whenever possible.", "Don't be alarmed when your cats bring you gifts of birds, mice or other wild critters. This is a gift, and they do it to please you.", "A smooth, shiny coat is the sign of a healthy cat.", "If you take kitten away from its mother before it is 8 weeks old, she may not have enough time to train it to use a litter box", "A healthy kitten has clear, bright eyes and clean ears.", "If your cat hides and then runs out and pounces on you, she is acting out her instinctive hunting ritual.", "Cats lick people as a sign of affection.", "Pregnant women are advised not to come in contact with cat faeces, because it can contain an organism which can affect the unborn child and even cause miscarriage.", "Most lively, active kittens grow up to be friendly, outgoing cats.", "A healthy cat's nose is cool.", "When a cat swishes its tail back and forth, she's concentrating on something; if her tail starts moving faster, she has become annoyed.", "Only a mother cat should pick a cat up by the scruff of the neck.", "Brushing your cat daily will cut down on hairballs.", "If you do not respond when your cat talks to you, it will soon lose the urge to communicate with you.", "Some cats, males in particular, develop health problems if fed dry food exclusively.", "A little vegetable oil daily will help to prevent fur-balls and bring a shine to your cat's coat.", "It has been scientifically proven that owning cats is good for our health and can decrease the occurrence of high blood pressure and other illnesses.", "Stroking a cat can help to relieve stress, and the feel of a purring cat on your lap conveys a strong sense of security and comfort.", "In multi-cat households, cats of the opposite sex usually get along better.", "25% of cat owners blow dry their cats hair after a bath.", "If your cat is near you, and her tail is quivering, this is the greatest expression of love your cat can give you.", "People who own pets live longer, have less stress, and have fewer heart attacks.", "'Sociable' cats will follow you from room to room to monitor your activities throughout the day.", "The more cats are spoken to, the more they will speak to you.", "Most cats prefer their food at room temperature", "95% of all cat owners admit they talk to their cats.", "If you can't feel your cat's ribs, she's too heavy.", "A cat that bites you after you have rubbed his stomach, is probably biting out of pleasure, not anger.", "Expect to spend an average of $80 per year on vet bills, for the lifetime of each cat you own.", "It costs $7000 to care for one household cat over its lifetime. This covers only the necessities; the pampered pet will carry a higher price.", "To make sure your cat's collar fits properly, make sure you can slip two fingers under the collar, between the collar and your cat's neck. ", "Cats lived with soldiers in trenches, where they killed mice during World War I.", "Napoleon was terrified of cats.", "Abraham Lincoln loved cats. He had four of them while he lived in the White House.", "The ancestor of all domestic cats is the African Wild Cat which still exists today", "In ancient Egypt, killing a cat was a crime punishable by death", "In ancient Egypt, mummies were made of cats, and embalmed mice were placed with them in their tombs. In one ancient city, over 300,000 cat mummies were found.", "In the Middle Ages, during the Festival of Saint John, cats were burned alive in town squares.", "In ancient Egypt, entire families would shave their eyebrows as a sign of mourning when the family cat died.", "The cat family split from the other mammals at least 40,000,000 years ago, making them one of the oldest mammalian families.", "Phoenician cargo ships are thought to have brought the first domesticated cats to Europe in about 900 BC", "Cats have been domesticated for half as long as dogs have been.", "The Pilgrims were the first to introduce cats to North America.", "The first breeding pair of Siamese cats arrived in England in 1884.", "The first formal cat show was held in England in 1871; in America, in 1895.", "The Maine Coon cat is America's only natural breed of domestic feline.", "The life expectancy of cats has nearly doubled since 1930 - from 8 to 16 years.", "Cat litter was 'invented' in 1947 when Edward Lowe asked his neighbour to try a dried, granulated clay used to sop up grease spills in factories.", "Genetic mutation created the domestic cat which is tame from birth.", "Among other tasks, cats can be taught to use a toilet, come, sit, beg, heel, jump through a hoop, play dead, roll over, open a door, shake, fetch and more", "A cat will not eat its food if is unable to smell it.", "Sir Isaac Newton is not only credited with the laws of gravity but is also credited with inventing the cat flap.", "There have been three different cats who have played the famed 'Morris the Cat.' The first Morris was adopted from a shelter in 1968. In 1969 he landed the role of Morris the Cat in the famous 9 Lives Cat Food commercials...and was an overnight success! The first Morris died in 1978 and was subsequently replaced by two more cats who played 'Morris.' All three of the 'Morris the Cat' cats were rescued from shelters.", "34% of cat-owning households have incomes of $60,000 or more.", "32% of those who own their own home, also own at least one cat. ", "If your cat rolls over on his back to expose his belly, it means he trusts you.", "Cats purr to communicate. Purring does not always mean happiness.", "Mother cats teach their kittens to use the litter box.", "Contrary to popular belief, the cat is a social animal.", "Some cats will actually knead and drool when they are petted. The kneading or marching means that the cat is happy", "Unlike humans and dogs, cats do not suffer a lot from loneliness. They are far more concerned with territorial issues.", "A cat will spend nearly 30% of her life grooming herself.", "Cats bury their faeces to cover their trails from predators.", "Hunting is not instinctive for cats. Kittens born to non-hunting mothers may never learn to hunt.", "Cats are attracted to the cave-like appeal of a clothes dryer.", "A cat will kill it's prey based on movement, but may not necessarily recognize that prey as food. Realizing that prey is food is a learned behaviour. ", "A group of kittens is called a kindle", "A group of adult cats is called a clowder", "When a domestic cat goes after mice, about one pounce in three results in a catch.", "The cheetah is the only cat in the world that can't retract it's claws.", "Studies show that if a cat falls off the seventh floor of a building it is 30% less likely to survive than a cat that falls off the twentieth floor. It supposedly takes about eight floors for the cat to realize what is occurring, relax and correct itself.", "A large majority of white cats with blue eyes are deaf. White cats with only one blue eye are deaf only in the ear closest to the blue eye. White cats with orange eyes do not have this disability.", "Today there are about 100 distinct breeds of the domestic cat.", "All cats are members of the family Felidea", "A domestic cat can sprint at about 31 miles per hour", "The catgut formerly used as strings in tennis rackets and musical instruments does not come from cats. Catgut actually comes from sheep, hogs, and horses", "Most deaf cats do not meow.", "In England, the government owns thousands of cats. Their job is to help keep the buildings free of rodents.", "Australia and Antarctica are the only continents which have no native cat species.", "Ailurophile is the word cat lovers are officially called.", "Calico cats are almost always female.", "A falling cat will always right itself in a precise order. First the head will rotate, then the spine will twist and the rear legs will align, then the cat will arch its back to lessen the impact of the landing.", "The most popular names for female cats in the U.S. are Missy, Misty, Muffin, Patches, Fluffy, Tabitha, Tigger, Pumpkin and Samantha.", "In English, cat is 'cat.' In French, cat is 'Chat.' In German, your cat is 'katze.' The Spanish word for cat is 'gato,' and the Italian word is 'gatto.' Japanese prefer 'neko' and Arabic countries call a cat a 'kitte.'", "It is believed that a white cat sitting on your doorstep just before your wedding is a sign of lasting happiness.", "Cats are more active during the evening hours.", "According to myth, a cat sleeping with all four paws tucked under means cold weather is coming.", "Hebrew folklore believes that cats came about because Noah was afraid that rats might eat all the food on the ark. He prayed to God for help. God responded by making the lion sneeze a giant sneeze -- and out came a little cat!"]


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
    nickname = 'Beep_bot'
    channels = ['#demo']
    password = ''


    def __init__(self):
        self.socket = socket.socket()
        self.socket.connect(('irc.freenode.net', 6667))
        self.send("NICK %s" % self.nickname)
        self.send("USER %(nick)s %(nick)s %(nick)s :%(nick)s" % {'nick':self.nickname})
        self.send("PRIVMSG nickserv :identify %s %s\r\n" % (self.nickname, self.password))
       
     # Add a list of nicks to send notifications and the nick of the owner 
    nickToCheck = ['add','nicks']
    owner = 'owner_nick'
   
    # Nick : TwiterId
    tweetID = {'add':'twitter_id','nicks':'twitter_id'}

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
               
                # Get nick of the person who sent a message
                sender = ctx['sender']
                sender_trim = re.compile(r"(!)")
                sendnick = sender_trim.split(sender)
                sendnick = sendnick[0]
               
           

                # whom to reply?
                target = ctx['target']
                if ctx['target'] == self.nickname:
                    target = ctx['sender'].split("!")[0]
                   
                                  
                # directed to the bot
                if ctx['type'] == 'PRIVMSG' and (ctx['msg'].lower()[0:len(self.nickname)] == self.nickname.lower() or ctx['target'] == self.nickname):
                    # something is speaking to the bot
                    query = ctx['msg']

                    if ctx['target'] != self.nickname:
                        try:
                            query = query[len(self.nickname):]
                            query = query.lstrip(':,;. ')
                        except:
                            print "Error : while I'm mentioned!"
                       
                    # do something intelligent here
                    print 'someone spoke to us: ', query
                    try:
                        rand_response = random.choice(responses)
                        self.say(rand_response, target)
                    except:
                        print "Something bad rolled in under the hood! Error while responding.."
               
                # some basic commands
                if ctx['msg'] == '!help':
                    try:
                        self.say('available commands: !help,!troll,!tweet,!excuse', target)
                    except:
                        print "Something bad rolled in under the hood! Error while helping..."

                if data.find('fuck') != -1:
                    try:
                        self.say(sendnick+", "+"Don't throw the word fuck anyhow", target)
                    except:
                        print "Error! 'Fuck notice' failed.."
                       
                if ctx['msg'] == '!troll':
                    try:
                        trolld = random.choice(troll)
                        self.say(trolld, target)
                    except:
                        print "Error! I can't troll.."
               
                # You can change sendnick value to your desired Nick
                if ctx['msg'].startswith('!tweet') and sendnick == owner:
                    try:
                        tweet_dat = ctx['msg'].strip('!tweet')
   
                        if len(tweet_dat) < 140 :
                            wrapper = TwitterWrapper(consumer_key, consumer_secret, access_token, access_token_secret)
                            wrapper.update_status(tweet_dat)
                    except:
                        print "Error!! I can't tweet.."
               
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
                           
                            else:                               
                                wrapper = TwitterWrapper(consumer_key, consumer_secret, access_token, access_token_secret)
                                wrapper.send_dm(tid, tmp)
                        except:
                            print "Error: I can't Sent a DM!"

                # check if !excuse command is issued, to send a random BOFH excuse
                if ctx['msg'] == '!excuse':
                    try:
                        excuse = random.choice(excuses)
                        self.say(excuse, target)
                    except:
                        print "Error: I can't make Excuses!"

                # Check if !fcat command is issued, to send a cat fact
                if ctx['msg'] == '!fcat':
                    try:
                        excuse = random.choice(fcat)
                        self.say(excuse, target)
                    except:
                        print "Error: Facts about Cats failed! Meow!"
               
                # Add A new User for alerts/notifications
                if ctx['msg'].startswith('!addbeep') and sendnick == owner:
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

                   
                # Remove User for alerts
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

