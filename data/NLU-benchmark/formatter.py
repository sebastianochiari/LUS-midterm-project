import os
import sys
import json

# constant for the selection of the file and file names
INTENT = 'SearchScreeningEvent'
TRAIN = 'train'
VALIDATE = 'validate'
TEST = 'test'
FULL = '_full'
DATA_DIR = 'original/2017-06-custom-intent-engines/' + INTENT + '/' + VALIDATE + '_' + INTENT + '.json'
OUTPUT_FILE_UTTERANCES = INTENT + '/' + INTENT + '.' + TEST + '.utterances.txt'
OUTPUT_FILE_CONLL = INTENT + '/' + INTENT + '.' + TEST + '.conll.txt'

# create folder
os.system('mkdir ' + INTENT)

# open all the necessary files
with open(DATA_DIR) as f:
    data = json.load(f)
# print(len(data[INTENT]))
output_utterances = open(OUTPUT_FILE_UTTERANCES, 'w')
output_conll = open(OUTPUT_FILE_CONLL, 'w')

for i in range(len(data[INTENT])):

    entry = ((data[INTENT])[i])['data']
    
    sentence = ''
    conll = ''
    
    for j in range(len(entry)):
        
        txt = (entry[j])['text']
        split_txt = txt.split()
        
        for k in range(len(split_txt)):
            
            sentence += split_txt[k] + ' '
            conll += split_txt[k] + '\t'
            
            if 'entity' in entry[j]:
                
                tag = (entry[j])['entity']
                
                if k == 0:
                    tag = 'B-' + tag
                else:
                    tag = 'I-' + tag
                conll += tag + '\n'

            else:
                conll += 'O' + '\n'
    
    sentence += '\n'
    conll += '\n'

    output_utterances.write(sentence)
    # print(sentence)

    output_conll.write(conll)
    # print(conll)

output_utterances.close()
output_conll.close()