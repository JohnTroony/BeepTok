
import cPickle as pickle
import random


def picks(filex, namex):

	with open(filex, 'rb') as input:
	    darn = pickle.load(input)
	    namex = random.choice(darn)
	    return namex

trolld = picks('pkl_data/bot_troll.pkl', 'troll')
print trolld

responses = picks('pkl_data/bot_responses.pkl', 'response')
print responses

excuses = picks('pkl_data/bot_excuses.pkl', 'excuse')
print excuses

fcats = picks('pkl_data/bot_fcat.pkl', 'fcat')
print fcats



