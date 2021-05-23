#!/bin/bash

TEST_PATH='../../data/NLU-benchmark/AddToPlaylist/AddToPlaylist.test.utterances.txt'

# generate FAR with all test sentences
farcompilestrings \
    --symbols=isyms.txt \
    --keep_symbols \
    --unknown_symbol='<UNK>' \
    $TEST_PATH tst.far

# create the working directory where to extract the .FAR file
wdir='wdir'
mkdir -p $wdir

# extract the sentences
farextract --filename_prefix="$wdir/" tst.far

farr=($(ls $wdir))

# cycle through and apply the tagging procedure
for f in ${farr[@]}
do
    fstcompose $wdir/$f w2t_mle.inv.bin | fstcompose - t1.lm |\
    fstshortestpath | fstrmepsilon | fsttopsort | fstprint --isymbols=isyms.txt 
done > w2t_mle.inv.txt

# run the evaluation script
python3 test.py

# results.csv formatting section
if [ $# -eq 2 ]
  then
    # change results.csv file name and move to the correct folder
    mkdir results
    mv results.csv results/results_order-$1_method-$2_cutoff-2.csv  
elif [ $# -eq 3 ]
  then
    # change results.csv file name and move to the correct folder
    mkdir results
    mv results.csv results/results_order-$1_method-$2_cutoff-$3.csv  
fi