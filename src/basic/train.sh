#!/bin/bash

# DATASET FILE PATH
DATASET_CONLL_PATH='../../data/NL2SparQL4NLU/NL2SparQL4NLU.train.conll.txt'

# check the input parameters
# python3 gateway.py $1 $2

# generate input and output lexicon
python3 train.py $3

# MLE (Maximum Likelihood Estimation) computation
# lets use our symbol tables (since they both have been applied cut-off)
cat isyms.txt osyms.t.txt | cut -f 1 | sort | uniq > msyms.m.lst.txt
ngramsymbols msyms.m.lst.txt msyms.t.txt

# let's convert data to ngrams
cat $DATASET_CONLL_PATH | sed '/^$/d' | awk '{print $2,$1}' > trn.w2t.txt

farcompilestrings \
    --symbols=msyms.t.txt \
    --keep_symbols \
    --unknown_symbol='<UNK>' \
    trn.w2t.txt trn.w2t.far

# count bigrams
ngramcount --order=2 trn.w2t.far trn.w2t.cnt
# make a model
ngrammake trn.w2t.cnt trn.w2t.lm
# print ngram info
# ngraminfo trn.w2t.lm

# print ngram probabilities as negative logs
ngramprint \
    --symbols=msyms.t.txt\
    --negativelogs \
    trn.w2t.lm trn.w2t.probs

# GENERATE LANGUAGE MODEL
# compile data into FAR again
farcompilestrings \
    --symbols=osyms.t.txt \
    --keep_symbols \
    --unknown_symbol='<UNK>' \
    trn.t.txt trn.t.far

# train the language model
ngramcount --order=$1 trn.t.far trn.t1.cnt
ngrammake --method=$2 trn.t1.cnt t1.lm
# print ngram info
# ngraminfo t1.lm

# GENERATE FST
python3 fst.py
echo "Generated FST"
# compile FST
fstcompile \
    --isymbols=osyms.t.txt \
    --osymbols=isyms.txt \
    --keep_isymbols \
    --keep_osymbols \
    trn.w2t_mle.txt w2t_mle.bin
# invert to have words on input
fstinvert w2t_mle.bin w2t_mle.inv.bin
# print FST info
# fstinfo w2t_mle.inv.bin | head -n 8
echo "Compiled FST"
