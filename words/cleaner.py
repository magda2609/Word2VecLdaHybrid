import re
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from gensim.parsing.preprocessing import STOPWORDS


def tokenize(files):
    allWordsConnectedToFiles = []
    for file in files:
        sentences = []
        for line in file:
            lettersOnly = re.sub("[^a-zA-Z]", " ", line)
            smallLetters = lettersOnly.lower()
            sentences.append(nltk.word_tokenize(smallLetters))
        sentences2 = []
        for line in sentences:
            for oneWord in line:
                if (oneWord not in stopwords.words('english')):
                    if (oneWord not in STOPWORDS):
                        try:
                            word = wordnet.synsets(oneWord)[0].lemmas()[0].name()
                            if (word not in stopwords.words('english')):
                                if (oneWord not in STOPWORDS):
                                    sentences2.append(word.lower())
                        except:
                            a=None
        allWordsConnectedToFiles.append(sentences2)
    return allWordsConnectedToFiles

def unique_words(words_in_documents):
    words = set([])
    for words_in_document in words_in_documents:
        for word in words_in_document:
            words.add(word)

    return list(words)