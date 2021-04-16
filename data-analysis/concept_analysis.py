import numpy as np 

def read_conll(file):
    tuples = []
    for line in file:
        tmp = list(line.split())
        if len(tmp) > 0:
            tuples.append(tmp)
    return tuples

def concept_distribution(input_list):
    tmp = {}
    total = 0
    for tuple in input_list:
        tmp[tuple[1]] = tmp.get(tuple[1], 0) + 1
        total += 1
    
    oov_perc = tmp['O'] / total * 100
    concept_perc = (1 - tmp['O'] / total) * 100

    tmp = sorted(tmp.items(), key=lambda x: x[1], reverse=True)
    return tmp, total, oov_perc, concept_perc

def print_to_csv(filename, toPrint):
    file_csv = open(filename + '.csv', 'w')
    head = "tag, counts\n"
    file_csv.write(head)
    for entry in toPrint:
	    tmp = entry[0] + ", " + str(entry[1]) + "\n"
	    file_csv.write(tmp)
    file_csv.close()

def print_to_txt(filename, toPrint):
    file_txt = open(filename + '.txt', 'a')
    file_txt.write(toPrint + '\n')
    file_txt.close()

def concept_analysis_CONLL(train_path, test_path):
    # read dataset files
    train = open(train_path, 'r')
    test = open(test_path, 'r')

    # extract all the tuples word-tag from the train file
    train_wordtag = read_conll(train)
    # extract all the tuples word-tag from the test file
    test_wordtag = read_conll(test)

    ## CONCEPTS DISTRIBUTION and OOV --------------------------- ##
    train_concepts, train_total_concepts, train_oov_perc, train_concept_perc = concept_distribution(train_wordtag)
    test_concepts, test_total_concepts, test_oov_perc, test_concept_perc = concept_distribution(test_wordtag)

    ## CSV EXPORT (for readability and infographics purposes) -- ##
    print_to_csv('train', train_concepts)
    print_to_csv('test', test_concepts)

    ## TXT EXPORT ---------------------------------------------- ##
    print_to_txt('train', 'OOV percentage: ' + str(train_oov_perc))
    print_to_txt('train', 'Concept percentage: ' + str(train_concept_perc))

    print_to_txt('test', 'OOV percentage: ' + str(test_oov_perc))
    print_to_txt('test', 'Concept percentage: ' + str(test_concept_perc))