#!/bin/bash

# 
farcompilestrings \
    --symbols=isyms.txt \
    --keep_symbols \
    --unknown_symbol='<UNK>' \
    ../../data/NL2SparQL4NLU/NL2SparQL4NLU.test.utterances.txt tst.far

# create the working directory where to extract the .FAR file
wdir='wdir'
mkdir -p $wdir

# extract the .FAR file
farextract --filename_prefix="$wdir/" tst.far

farr=($(ls $wdir))

# cycle through and apply the sequence labelling
for f in ${farr[@]}
do
    fstcompose $wdir/$f w2t_mle.inv.bin | fstcompose - t1.lm |\
    fstshortestpath | fstrmepsilon | fsttopsort | fstprint --isymbols=isyms.txt 
done > w2t_mle.inv.txt

# run the evaluation script
python3 test.py