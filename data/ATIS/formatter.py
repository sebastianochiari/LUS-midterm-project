import os
import pickle

DATA_DIR = "original/data/raw_data/ms-cntk-atis"

print(os.listdir(DATA_DIR))

def load_ds(fname='atis.train.pkl'):
    with open(fname, 'rb') as stream:
        ds, dicts = pickle.load(stream)
    print('Done  loading: ', fname)
    print('      samples: {:4d}'.format(len(ds['query'])))
    print('   vocab_size: {:4d}'.format(len(dicts['token_ids'])))
    print('   slot count: {:4d}'.format(len(dicts['slot_ids'])))
    print(' intent count: {:4d}'.format(len(dicts['intent_ids'])))
    return ds, dicts

def removeTags(query):
    tmp = query.split()
    sent = ''
    for i in range(1, len(tmp) - 1):
        sent += tmp[i] + ' '
    return sent 

train_ds, dicts = load_ds(os.path.join(DATA_DIR, 'atis.train.pkl'))
test_ds, dicts = load_ds(os.path.join(DATA_DIR, 'atis.test.pkl'))

t2i, s2i, in2i = map(dicts.get, ['token_ids', 'slot_ids', 'intent_ids'])
i2t, i2s, i2in = map(lambda d: {d[k]: k for k in d.keys()}, [t2i, s2i, in2i])
query, slots, intent = map(train_ds.get,
                           ['query', 'slot_labels', 'intent_labels'])

# TRAIN FILES
train_utt = open('ATIS.train.utterances.txt', 'w')
train_conll = open('ATIS.train.conll.txt', 'w')

for i in range(len(query)):
    # UTTERANCES FILE
    sentence = '{}'.format(' '.join(map(i2t.get, query[i])))
    sentence = removeTags(sentence)
    train_utt.write(sentence + '\n')

    # CONLL FILE
    for j in range(1, len(query[i]) - 1):
        entry = i2t[query[i][j]] + '\t' + i2s[slots[i][j]]
        train_conll.write(entry + '\n')
    train_conll.write('\n')

train_utt.close()
train_conll.close()

# TEST FILES
query, slots, intent = map(test_ds.get,
                           ['query', 'slot_labels', 'intent_labels'])

test_utt = open('ATIS.test.utterances.txt', 'w')
test_conll = open('ATIS.test.conll.txt', 'w')

for i in range(len(query)):
    # UTTERANCES FILE
    sentence = '{}'.format(' '.join(map(i2t.get, query[i])))
    sentence = removeTags(sentence)
    test_utt.write(sentence + '\n')

    # CONLL FILE
    for j in range(1, len(query[i]) - 1):
        entry = i2t[query[i][j]] + '\t' + i2s[slots[i][j]]
        test_conll.write(entry + '\n')
    test_conll.write('\n')

test_utt.close()
test_conll.close()