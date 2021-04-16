import numpy as np 
from concept_analysis import concept_analysis_CONLL
from corpus import corpus_main

train = './data/NL2SparQL4NLU/NL2SparQL4NLU.train.utterances.txt'
test = './data/NL2SparQL4NLU/NL2SparQL4NLU.test.utterances.txt'

corpus_main(train, test)

trainCONLL = './data/NL2SparQL4NLU/NL2SparQL4NLU.train.conll.txt'
testCONLL = './data/NL2SparQL4NLU/NL2SparQL4NLU.test.conll.txt'

concept_analysis_CONLL(trainCONLL, testCONLL)