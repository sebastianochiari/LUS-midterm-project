#!/bin/bash

# remove all the temporary files and folders generated during train and test

rm -f *.fst
rm -f *.far
rm -f *.fsa
rm -f *.cnt
rm -f *.lm
rm -f isyms.txt
rm -f osyms.*
rm -f msyms.*
rm -f *.trn.txt
rm -f trn.*
rm -rf wdir
rm -f *.out
rm -f w2t_*

clear