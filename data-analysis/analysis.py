import numpy as np 
from concept_analysis import concept_analysis_CONLL
from corpus import corpus_main

train = './data/NLU-benchmark/GetWeather/GetWeather.train.utterances.txt'
test = './data/NLU-benchmark/GetWeather/GetWeather.test.utterances.txt'

corpus_main(train, test)

trainCONLL = './data/NLU-benchmark/GetWeather/GetWeather.train.conll.txt'
testCONLL = './data/NLU-benchmark/GetWeather/GetWeather.test.conll.txt'

concept_analysis_CONLL(trainCONLL, testCONLL)