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
# Test kalimat pertama
kalimat = "Richard Winger , rekan di Boston Consulting Group , menambahkan : Belakangan ini , sangat populer jika menghias diri anda dengan bendera ."
print beautify(get_only_str(tree_to_str(chunk_me(kalimat))))

# output: [Richard Winger] [,] [rekan] [di Boston Consulting Group] [,] [menambahkan] [:] [Belakangan ini] [,] [sangat] [populer] [jika] [menghias] [diri] [anda] [dengan bendera] [.] 

# Test kalimat kedua
kalimat = "Indeks Keuangan dari 100 laba bank-bank dan peruhaan asuransi terbesar menambah 2,19 menjadi 447,76 ."
print beautify(get_only_str(tree_to_str(chunk_me(kalimat))))

# output: [Indeks Keuangan] [dari 100 laba] [bank-bank] [dan] [peruhaan asuransi terbesar] [menambah] [2,19] [menjadi 447,76] [.] 
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