import os.path

def loadCorpus(file):
    """
    create the corpus as list of lists from a given file
    :param file: input file to read
    :return: list of lists with the single words from the given file
    """
    # read the file
    if not os.path.isfile(file):
        print('File does not exist.')
    else:
        with open(file) as f:
            content = f.read().splitlines()
            
    # creating the storing variable
    corpus = [ [] for _ in range(len(content)) ]
    
    # check the corpus line by line
    i = 0
    for line in content:
        txt = line;
        temp = txt.split()
        corpus[i] = temp
        i += 1

    return corpus

def descriptiveStatistics(corpus):
    """
    compute corpus descriptive statistics (total utterances and word counts)
    :param file: input file to read
    """
    
    # total words
    total_words = 0
    for i in range(len(corpus)):
        total_words += len(corpus[i])
    
    # utterances
    total_utterances = len(corpus)

    return total_words, total_utterances

def computeLexicon(corpus):
    """
    compute a lexicon from corpus in a list-of-list format
    :param corpus: the corpus from which we want to extract the lexicon
    :return: the alphabetically ordered set of lexicon
    """
    lexicon = set()
    for i in range(len(corpus)):
        for j in range(len(corpus[i])):
            lexicon.add(corpus[i][j])
    sorted(lexicon)
    return lexicon

def computeFrequencyListFromLexicon(corpus, lexicon):
    """
    compute the frequency list from lexicon
    :param lexicon: input lexicon
    :return: the dictonary which contains the frequency list of the words inside the corpus
    """
    
    # create the dictonary
    frequency_list = dict()
    for word in lexicon:
        frequency_list[word] = 0
    
    # fill the dictonary
    for i in range(len(corpus)):
        for j in range(len(corpus[i])):
            tmp = corpus[i][j]
            frequency_list[tmp] += 1
    return frequency_list

def corpus_main(train_path, test_path):
    
    # load train and test files and create the corpus
    train_corpus = loadCorpus(train_path)
    test_corpus = loadCorpus(test_path)

    # retrieve meaningful info
    train_words, train_utterances = descriptiveStatistics(train_corpus)
    train_lexicon = computeLexicon(train_corpus)
    train_frequencyList = computeFrequencyListFromLexicon(train_corpus, train_lexicon)

    file_txt = open('train.txt', 'w')
    file_txt.write(train_path + '\n' + 'Total words: ' + str(train_words) + '\n' + 'Total utterances: ' + str(train_utterances) + '\n')
    file_txt.write('Unique words: ' + str(len(train_lexicon)) + '\n')
    file_txt.close()

    test_words, test_utterances = descriptiveStatistics(test_corpus)
    test_lexicon = computeLexicon(test_corpus)
    test_frequencyList = computeFrequencyListFromLexicon(test_corpus, test_lexicon)

    file_txt = open('test.txt', 'w')
    file_txt.write(test_path + '\n' + 'Total words: ' + str(test_words) + '\n' + 'Total utterances: ' + str(test_utterances) + '\n')
    file_txt.write('Unique words: ' + str(len(test_lexicon)) + '\n')
    file_txt.close()