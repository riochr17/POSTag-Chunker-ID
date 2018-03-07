# POSTag dan Chunker Bahasa Indonesia

POSTagger (Part of Speech Tagger) dengan metode HMM menggunakan korpus [**One Million POS Tagged Corpus of Bahasa Indonesia**](http://panl10n.net/english/OutputsIndonesia2.htm) dan Chunker dengan metode Rule Based menggunakan rule yang didapat dari [**InaNLP (paper)**](http://ieeexplore.ieee.org/document/7803103/)

## Installation

Pastikan ada `nltk`

## Usage

```
$ -- Training POSTagger
$ python train_postag.py

$ -- Test POSTagger & Chunker
$ python main.py
```

```python
ch = Chunker()
kalimat = "Richard Winger , rekan di Boston Consulting Group , menambahkan : Belakangan ini , sangat populer jika menghias diri anda dengan bendera ."

# Terdapat 3 jenis chunker berdasarkan POS Tagger yang digunakan

# Chunker dengan POS Tagger HMM menggunakan data One Million POS Taggged Corpus of Bahasa Indonesia
print ch.tree_to_str(ch.chunk_me1(kalimat))

# Chunker dengan POS Tagger HMM menggunakan data idn-tagged-corpus
print ch.tree_to_str(ch.chunk_me2(kalimat))

# Chunker dengan POS Tagger pretrained model CRFTagger
print ch.tree_to_str(ch.chunk_me3(kalimat))

# cara ketika terlihat lebih baik
```


Saya menyediakan sebuah live server untuk mengakses chunker ini lewat API 
dengan format request sebagai berikut:
```
POST /chunk HTTP/1.1
Host: rio.southeastasia.cloudapp.azure.com:5000
Content-Type: application/json

{
	"kalimat":"Indeks Keuangan dari 100 laba bank-bank dan peruhaan asuransi terbesar menambah 2,19 menjadi 447,76 ."
}
```

dan response
```
POST /chunk HTTP/1.1
Host: rio.southeastasia.cloudapp.azure.com:5000
Content-Type: text/html

[(u'Indeks Keuangan', u'NP'), (u'dari', 'IN'), (u'100', 'CD'), (u'laba bank-bank dan peruhaan asuransi terbesar', u'NP'), (u'menambah', 'VB'), (u'2,19', 'CD'), (u'menjadi', 'VB'), (u'447,76', 'CD'), (u'.', 'Z')]
```



## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## Credits

One Million POS Taggged Corpus of Bahasa Indonesia

http://panl10n.net/english/OutputsIndonesia2.htm

InaNLP (paper)

http://ieeexplore.ieee.org/document/7803103/

HMM-PoS-Tagger

https://github.com/rickardlofberg/HMM-PoS-Tagger

idn-tagged-corpus

https://github.com/famrashel/idn-tagged-corpus

POS Tagger Bahasa Indonesia dengan Python

https://yudiwbs.wordpress.com/2018/02/20/pos-tagger-bahasa-indonesia-dengan-pytho/
