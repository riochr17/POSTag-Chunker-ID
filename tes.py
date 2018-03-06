from nltk.tag import CRFTagger
try:
    import pycrfsuite
except ImportError:
    pass
    print "ga ketemu"

ct = CRFTagger() 
ct.set_model_file('dataset/all_indo_man_tag_corpus_model.crf.tagger')
hasil = ct.tag_sents([[unicode('Saya'),unicode('bekerja'),unicode('di'),unicode('Bandung')]])
print(hasil)
