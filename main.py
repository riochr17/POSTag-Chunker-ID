import re
import nltk
import pickle
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tree import Tree
from probCalc import probability as PB
from tagger import Tagger

UNIQ='_UNIQUE_STRING_'
CHUNK_PARSER = None

"""
"""
def load_obj(name):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

"""
"""
class MarkPlaceholders(dict):
	def __getitem__(self, key):
		return UNIQ+('(?P<%s>.*?)'%key)+UNIQ

"""
Melakukan formatting string menjadi regex
"""
def format_to_re(format):
	parts = (format % MarkPlaceholders()).split(UNIQ)
	for i in range(0, len(parts), 2):
		parts[i] = re.escape(parts[i])

	return ''.join(parts).replace('\\', '')

"""
Mengubah tree POS Tag menjadi tree chunk
"""
def tree_to_str(tree_data):
	ne_in_sent = []
	for subtree in tree_data:
		if type(subtree) == Tree: # If subtree is a noun chunk, i.e. NE != "O"
			ne_label = subtree.label()
			ne_string = " ".join([token for token, pos in subtree.leaves()])
			ne_in_sent.append((ne_string, ne_label))
		else:
			ne_in_sent.append((subtree[0], subtree[1]))

	return ne_in_sent

"""
Memuat rule chunk
"""
def load_chunker():
	global CHUNK_PARSER
	try:
		f = open('dataset/phrase_chunker_grammar_id.txt')
		files = format_to_re(f.read())
		grammars = files
		f.close()
		
		CHUNK_PARSER = nltk.RegexpParser(grammars)

	except Exception as e:
		print str(e)

"""
Mengubah tree chunk menjadi list of chunk
dalam bentuk list of string
"""
def get_only_str(tree_chunk):
	output = []
	for chunk, tag in tree_chunk:
		output.append(chunk)

	return output

"""
Mengubah list of chunk(string) menjadi string
dengan format: [chunk1] [chunk2] ... [chunkN]
"""
def beautify(chunks):
	strout = ""
	for s in chunks:
		strout += "[" + s + "] "

	return strout

"""
Memberi POSTag pada setiap kata pada kalimat
Melakukan chunking kalimat
Mengembalikan chunk Tree
"""
def chunk_me(_str):
	return CHUNK_PARSER.parse(TAGGER.tagSentence(_str.split(" ")))

# Memuat data pre-trained POS-Tagger
uni, bi, tri, word = load_obj("tagger")
TAGGER = Tagger(uni, bi, tri, word)

# Memuat data grammar chunker
load_chunker()

# Test kalimat pertama
kalimat = "Richard Winger , rekan di Boston Consulting Group , menambahkan : Belakangan ini , sangat populer jika menghias diri anda dengan bendera ."
print beautify(get_only_str(tree_to_str(chunk_me(kalimat))))

# Test kalimat kedua
kalimat = "Indeks Keuangan dari 100 laba bank-bank dan peruhaan asuransi terbesar menambah 2,19 menjadi 447,76 ."
print beautify(get_only_str(tree_to_str(chunk_me(kalimat))))



