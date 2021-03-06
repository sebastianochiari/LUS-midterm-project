import pandas as pd 
from utils import read_corpus_conll, read_fst4conll
from conll import evaluate

test_path_CONLL = '../../data/NL2SparQL4NLU/NL2SparQL4NLU.test.conll.txt'

refs = read_corpus_conll(test_path_CONLL)
hyps = read_fst4conll('w2wt_wt.wt2.out', split=True)

results = evaluate(refs, hyps)

pd_tbl = pd.DataFrame().from_dict(results, orient='index')
pd_tbl.round(decimals=3)
pd_tbl.to_csv(r'./results.csv', sep=',', index=True, header=True)