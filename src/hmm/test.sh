#!/bin/bash

TEST_PATH='../../data/NL2SparQL4NLU/NL2SparQL4NLU.test.utterances.txt'

# generate FAR with all test sentences
farcompilestrings \
    --symbols=isyms.wt.txt \
    --keep_symbols \
    --unknown_symbol='<UNK>' \
    $TEST_PATH tst.wt.far

# create the working directory where to extract the .FAR file
wdir='wdir'
mkdir -p $wdir

# extract the sentences
farextract --filename_prefix="$wdir/" tst.wt.far

farr=($(ls $wdir))

for f in ${farr[@]}
do
    fstcompose $wdir/$f w2wt_wt.bin | fstcompose - wt2.lm |\
    fstshortestpath | fstrmepsilon | fsttopsort | fstprint --isymbols=isyms.wt.txt
done > w2wt_wt.wt2.out

# run the evaluation script
python3 test.py