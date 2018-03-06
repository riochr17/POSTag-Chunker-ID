from chunker import Chunker

ch = Chunker()
kalimat = "Richard Winger , rekan di Boston Consulting Group , menambahkan : Belakangan ini , sangat populer jika menghias diri anda dengan bendera ."
print ch.tree_to_str(ch.chunk_me2(kalimat))