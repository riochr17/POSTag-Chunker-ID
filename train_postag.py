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


"""
"""
def train_postag2(corpus="dataset/postag_ui.txt"):
	global TAGGER
	data = []

	print "read file..."
	f = open(corpus)
	lines = f.read().split('\n\n')
	f.close()

	for line in lines:
		fx_line = line.split('\n')

		sen_tag = []
		for _word in fx_line:
			word_tag = _word.split("\t")
			word = word_tag[0]
			tag  = word_tag[1]
			sen_tag.append((word, tag))

		data.append(sen_tag)

	print "end read file"
	print "training pos tagger..."
	save_obj(PB(data), "tagger2")
	print "end training pos tagger"

train_postag2()