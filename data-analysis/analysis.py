import numpy as np 
from concept_analysis import concept_analysis_CONLL
from corpus import corpus_main

train = './data/ATIS/ATIS.train.utterances.txt'
test = './data/ATIS/ATIS.test.utterances.txt'

corpus_main(train, test)

trainCONLL = './data/ATIS/ATIS.train.conll.txt'
testCONLL = './data/ATIS/ATIS.test.conll.txt'

concept_analysis_CONLL(trainCONLL, testCONLL)