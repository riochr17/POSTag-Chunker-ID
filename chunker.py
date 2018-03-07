import re
import nltk
import pickle
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tree import Tree
from probCalc import probability as PB
from tagger import Tagger

from nltk.tag import CRFTagger
try:
    import pycrfsuite
except ImportError:
    pass
    print "ga ketemu"


"""
"""
class MarkPlaceholders(dict):
	self.UNIQ='_UNIQUE_STRING_'
	def __getitem__(self, key):
		return self.UNIQ+('(?P<%s>.*?)'%key)+self.UNIQ

"""
"""
class Chunker:
	UNIQ='_UNIQUE_STRING_'
	CHUNK_PARSER = None

	"""
	"""
	def __init__(self):
		# Memuat data pre-trained POS-Tagger
		uni, bi, tri, word = self.load_obj("tagger")
		self.TAGGER1 = Tagger(uni, bi, tri, word)

		# Memuat data pre-trained POS-Tagger
		uni2, bi2, tri2, word2 = self.load_obj("tagger2")
		self.TAGGER2 = Tagger(uni2, bi2, tri2, word2)

		self.TAGGER3 = CRFTagger()
		self.TAGGER3.set_model_file('dataset/all_indo_man_tag_corpus_model.crf.tagger')

		# Memuat data grammar chunker
		self.load_chunker()

	"""
	"""
	def load_obj(self, name):
	    with open('obj/' + name + '.pkl', 'rb') as f:
	        return pickle.load(f)

	"""
	Melakukan formatting string menjadi regex
	"""
	def format_to_re(self, format):
		parts = (format % MarkPlaceholders()).split(self.UNIQ)
		for i in range(0, len(parts), 2):
			parts[i] = re.escape(parts[i])

		return ' '.join(parts).replace('\\', '')

	"""
	Mengubah tree POS Tag menjadi tree chunk
	"""
	def tree_to_str(self, tree_data):
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
	def load_chunker(self):
		try:
			f = open('dataset/phrase_chunker_grammar_id.txt')
			files = self.format_to_re(f.read())
			grammars = files
			f.close()
			
			self.CHUNK_PARSER = nltk.RegexpParser(grammars)

		except Exception as e:
			print str(e)

	"""
	Mengubah tree chunk menjadi list of chunk
	dalam bentuk list of string
	"""
	def get_only_str(self, tree_chunk):
		output = []
		for chunk, tag in tree_chunk:
			output.append(chunk)

		return output

	"""
	Mengubah list of chunk(string) menjadi string
	dengan format: [chunk1] [chunk2] ... [chunkN]
	"""
	def beautify(self, chunks):
		strout = ""
		for s in chunks:
			strout += "[" + s + "] "

		return strout

	"""
	Memberi POSTag pada setiap kata pada kalimat
	Melakukan chunking kalimat
	Mengembalikan chunk Tree
	"""
	def chunk_me1(self, _str):
		return self.CHUNK_PARSER.parse(self.TAGGER1.tagSentence(_str.split(" ")))

	"""
	Memberi POSTag pada setiap kata pada kalimat
	Melakukan chunking kalimat
	Mengembalikan chunk Tree
	"""
	def chunk_me2(self, _str):
		return self.CHUNK_PARSER.parse(self.TAGGER2.tagSentence(_str.split(" ")))

	"""
	"""
	def chunk_me3(self, _str):
		_strs = _str.split(" ")
		strs = []
		for s in _strs:
			strs.append(unicode(s))

		return self.CHUNK_PARSER.parse(self.TAGGER3.tag_sents([strs])[0])


	# # Test kalimat pertama
	# kalimat = "Richard Winger , rekan di Boston Consulting Group , menambahkan : Belakangan ini , sangat populer jika menghias diri anda dengan bendera ."
	# print beautify(get_only_str(tree_to_str(chunk_me2(kalimat))))

	# # Test kalimat kedua
	# kalimat = "Indeks Keuangan dari 100 laba bank-bank dan peruhaan asuransi terbesar menambah 2,19 menjadi 447,76 ."
	# print beautify(get_only_str(tree_to_str(chunk_me2(kalimat))))

	# # Test kalimat ketiga
	# kalimat = "Binatang ini tidak bisa dibunuh karena masyarakat India menganggap mereka suci ."
	# print beautify(get_only_str(tree_to_str(chunk_me2(kalimat))))

	# # Test kalimat ketiga
	# kalimat = "Pemkot telah menempatkan ikan di berbagai genangan air untuk memangsa telur nyamuk ."
	# print beautify(get_only_str(tree_to_str(chunk_me2(kalimat))))

	# # Test kalimat ketiga
	# kalimat = "Seorang juru bicara bagi pasukan pimpinan Hamas tak bisa diperoleh komentar -nya mengenai hal itu ."
	# print beautify(get_only_str(tree_to_str(chunk_me2(kalimat))))

	# # Test kalimat ketiga
	# kalimat = "Pengacara Tyson , Tom Marlowe belum dapat dimintai konfirmasi ."
	# print beautify(get_only_str(tree_to_str(chunk_me2(kalimat))))



