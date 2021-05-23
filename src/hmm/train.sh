#!/bin/bash

# DATASET FILE PATH
DATASET_CONLL_PATH='../../data/NL2SparQL4NLU/NL2SparQL4NLU.train.conll.txt'

# generate input and output lexicon
python3 train.py $3

# compile data into FAR
farcompilestrings \
    --symbols=osyms.wt.txt \
    --keep_symbols \
    --unknown_symbol='<UNK>' \
    trn.wt.txt trn.wt.far

# train ngram model
ngramcount --order=2 trn.wt.far trn.wt.cnt
ngrammake trn.wt.cnt wt2.lm
ngraminfo wt2.lm

# GENERATE FST
python3 fst.py
echo "Generated FST"
# compile FST
fstcompile \
    --isymbols=isyms.wt.txt \
    --osymbols=osyms.wt.txt \
    --keep_isymbols \
    --keep_osymbols \
    w2wt_wt.txt w2wt_wt.bin
fstinfo w2wt_wt.bin | head -n 8
echo "Compiled FST"
