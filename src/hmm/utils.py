"""
Utility function container
"""

import re
from math import log

def read_corpus(corpus_file):
    """
    read corpus into a list-of-lists, splitting sentences into tokens by space (' ')
    :param corpus_file: corpus file in sentence-per-line format (tokenized)
    """
    return [line.strip().split() for line in open(corpus_file, 'r')]

def read_corpus_conll(corpus_file, fs="\t"):
    """
    read corpus in CoNLL format
    :param corpus_file: corpus in conll format
    :param fs: field separator
    :return: corpus
    """
    featn = None  # number of features for consistency check
    sents = []  # list to hold words list sequences
    words = []  # list to hold feature tuples

    for line in open(corpus_file):
        line = line.strip()
        if len(line.strip()) > 0:
            feats = tuple(line.strip().split(fs))
            if not featn:
                featn = len(feats)
            elif featn != len(feats) and len(feats) != 0:
                raise ValueError("Unexpected number of columns {} ({})".format(len(feats), featn))

            words.append(feats)
        else:
            if len(words) > 0:
                sents.append(words)
                words = []
    return sents

def get_column(corpus, column=-1):
    """
    get column from loaded corpus
    """
    return [[word[column] for word in sent] for sent in corpus]

def compute_frequency_list(corpus):
    """
    create frequency list for a corpus
    :param corpus: corpus as list of lists
    """
    frequencies = {}
    for sent in corpus:
        for token in sent:
            frequencies[token] = frequencies.setdefault(token, 0) + 1
    return frequencies

def cutoff(corpus, tf_min=2):
    """
    apply min cutoffs
    :param tf_min: minimum token frequency for lexicon elements (below removed); default 2
    :return: lexicon as set
    """
    frequencies = compute_frequency_list(corpus)
    return sorted([token for token, frequency in frequencies.items() if frequency >= tf_min])

def make_w2t_wt(isyms, sep='+', out='w2wt.tmp'):
    special = {'<epsilon>', '<s>', '</s>'}
    oov = '<UNK>'  # unknown symbol
    state = '0'    # wfst specification state
    fs = " "       # wfst specification column separator
    
    ist = sorted(list(set([line.strip().split("\t")[0] for line in open(isyms, 'r')]) - special))
    
    with open(out, 'w') as f:
        for e in ist:
            f.write(fs.join([state, state, e.split('+')[0], e]) + "\n")
        f.write(state + "\n")

# modified version to support fst-output
def read_fst4conll(fst_file, fs="\t", oov='<UNK>', otag='O', sep='+', split=False):
    """
    :param corpus_file: corpus in conll format
    :param fs: field separator
    :param oov: token to map to otag (we need to get rid of <unk> in labels)
    :param otag: otag symbol
    :param sep: 
    :param split:
    :return: corpus 
    """
    sents = []  # list to hold words list sequences
    words = []  # list to hold feature tuples

    for line in open(fst_file):
        line = line.strip()
        if len(line.strip()) > 0:
            feats = tuple(line.strip().split(fs))
            # arc has minimum 3 columns, else final state
            if len(feats) >= 3:
                ist = feats[2]  # 3rd column (input)
                ost = feats[3]  # 4th column (output)
                # replace '<unk>' with 'O'
                ost = otag if ost == oov else ost
                # ignore for now
                ost = ost.split(sep)[1] if split and ost != otag else ost
                
                words.append((ist, ost))
            else:
                sents.append(words)
                words = []
        else:
            if len(words) > 0:
                sents.append(words) 
                words = []
    return sents