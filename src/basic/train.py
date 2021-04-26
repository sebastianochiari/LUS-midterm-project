import os
import sys
from utils import read_corpus, cutoff, read_corpus_conll, get_column

# files management
train_path = '../../data/NL2SparQL4NLU/NL2SparQL4NLU.train.utterances.txt'
train_path_CONLL = '../../data/NL2SparQL4NLU/NL2SparQL4NLU.train.conll.txt'

# CUTOFF MANAGEMENT
CUTOFF = 2
if(len(sys.argv) == 2):
    CUTOFF = int(sys.argv[1])

# read corpus from utterances file
train_data = read_corpus(train_path)

# create train-lexicon with the specified cutoff
train_lexicon = cutoff(train_data, CUTOFF)

# write train-lexicon to file
with open('isyms.trn.txt', 'w') as f:
    f.write("\n".join(train_lexicon) + "\n")

# creates lexicon (with <UNK> tag)
os.system('ngramsymbols isyms.trn.txt isyms.txt')
os.system('echo "Generated input lexicon"')

# create training data in utterance-per-line format for output symbols (t - tags)
trn = read_corpus_conll(train_path_CONLL)
tags = get_column(trn, column=-1)

# write data
with open('trn.t.txt', 'w') as f:
    for s in tags:
        f.write(" ".join(s) + "\n")
        
tags_lexicon = cutoff(tags, CUTOFF)
with open('osyms.t.lst.txt', 'w') as f:
    f.write("\n".join(tags_lexicon) + "\n")

# creates tags lexicon (with <UNK> tag)
os.system('ngramsymbols osyms.t.lst.txt osyms.t.txt')
os.system('echo "Generated output lexicon"')