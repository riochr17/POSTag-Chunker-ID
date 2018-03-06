import re
import nltk
import pickle
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tree import Tree
from probCalc import probability as PB
from tagger import Tagger

UNIQ='_UNIQUE_STRING_'

"""
"""
def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'wb+') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

"""
"""
def train_postag(corpus="dataset/postagged.txt"):
	global TAGGER
	data = []

	r = re.compile(r"""\\(.)""")

	f = open(corpus)
	lines = f.read().split('\n')
	f.close()

	for line in lines:
		fx_line = r.sub(r'\1', line)

		sen_tag = []
		for word_tag in fx_line.split(" "):
			splitter_index = word_tag.rfind("/")
			word = word_tag[:splitter_index]
			tag  = word_tag[splitter_index + 1:]
			sen_tag.append((word, tag))

		data.append(sen_tag)

	save_obj(PB(data), "tagger")

train_postag()