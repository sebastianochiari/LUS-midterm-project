import os
import sys
from utils import read_corpus, cutoff, read_corpus_conll

# files management
train_path_CONLL = '../../data/NL2SparQL4NLU/NL2SparQL4NLU.train.conll.txt'

# CUTOFF MANAGEMENT
CUTOFF = 2
if(len(sys.argv) == 2):
    CUTOFF = int(sys.argv[1])

# read corpus from CONLL file
train_data_CONLL = read_corpus_conll(train_path_CONLL)

wt_sents = [["+".join(w) for w in s] for s in train_data_CONLL]
wt_osyms = cutoff(wt_sents, CUTOFF)
wt_isyms = [w.split('+')[0] for w in wt_osyms]

# write train-lexicon to file
with open('trn.wt.txt', 'w') as f:
    for s in wt_sents:
        f.write(" ".join(s) + "\n")

with open('isyms.wt.lst.txt', 'w') as f:
    f.write("\n".join(wt_isyms) + "\n")

# creates lexicon (with <UNK> tag)
os.system('ngramsymbols isyms.wt.lst.txt isyms.wt.txt')
os.system('echo "Generated input lexicon"')

with open('osyms.wt.lst.txt', 'w') as f:
    f.write("\n".join(wt_osyms) + "\n")

# creates tags lexicon (with <UNK> tag)
os.system('ngramsymbols osyms.wt.lst.txt osyms.wt.txt')
os.system('echo "Generated output lexicon"')