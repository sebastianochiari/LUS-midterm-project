"""
Python script to refactor the conll.txt files in order
to remove the O tags by replacing them with O-word
"""

from utils import read_corpus_conll

DATA_FOLDER = '../../data/NL2SparQL4NLU/'
TRAIN_CONLL = 'NL2SparQL4NLU.train.conll.txt'
TEST_CONLL = 'NL2SparQL4NLU.test.conll.txt'

train_path_CONLL = DATA_FOLDER + TRAIN_CONLL
test_path_CONLL = DATA_FOLDER + TEST_CONLL

trn_conll = read_corpus_conll(train_path_CONLL)
tst_conll = read_corpus_conll(test_path_CONLL)

train_conll = open('./' + TRAIN_CONLL, 'w')
test_conll = open('./' + TEST_CONLL, 'w')

for sentence in trn_conll:
    for entry in sentence:
        new_line = entry[0] + '\t'
        if (entry[1] == 'O'):
            new_line += 'O' + '-' + entry[0]
        else:
            new_line += entry[1]
        train_conll.write(new_line + '\n')
    train_conll.write('\n')

for sentence in tst_conll:
    for entry in sentence:
        new_line = entry[0] + '\t'
        if (entry[1] == 'O'):
            new_line += 'O' + '-' + entry[0]
        else:
            new_line += entry[1]
        test_conll.write(new_line + '\n')
    test_conll.write('\n')

train_conll.close()
test_conll.close()
