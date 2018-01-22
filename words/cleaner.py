import re
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from gensim.parsing.preprocessing import STOPWORDS


def tokenize(files, logger):
    allWordsConnectedToFiles = []
    i = 0
    size = len(files)
    for file in files:
        if (i % 250 == 1):
            logger.info("Tokenization - "+str(i)+" over "+ str(size))
            logger.info("And now there is "+str(allWordsConnectedToFiles.__sizeof__())+" words")
        i = i+1
        sentences = []
        for line in file:
            lettersOnly = re.sub("[^a-zA-Z]", " ", line)
            smallLetters = lettersOnly.lower()
            sentences.append(nltk.word_tokenize(smallLetters))
        sentences2 = []
        for line in sentences:
            for oneWord in line:
                try:
                    word = wordnet.synsets(oneWord)[0].lemmas()[0].name()
                    if (word not in stopwords.words('english')):
                        if (oneWord not in STOPWORDS):
                            sentences2.append(word.lower())
                except:
                    a=None
        # if (sentences2.__sizeof__() > 0):
        allWordsConnectedToFiles.append(sentences2)
    return allWordsConnectedToFiles

def unique_words(words_in_documents):
    words = set([])
    for words_in_document in words_in_documents:
        for word in words_in_document:
            words.add(word)

    return list(words)
