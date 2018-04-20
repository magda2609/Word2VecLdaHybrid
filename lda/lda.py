from gensim.models.ldamodel import LdaModel
from gensim.corpora import Dictionary, MmCorpus
from gensim.utils import ClippedCorpus

def lda(words, topics):
    dictionary = Dictionary(words)
    dictionary.save('documents.dict')
    corpus = [dictionary.doc2bow(text) for text in words]
    MmCorpus.serialize('documents.mm', corpus)
    mm_corpus = MmCorpus('documents.mm')

    mm = ClippedCorpus(mm_corpus)


    lda = LdaModel(corpus=mm, id2word=dictionary, num_topics=topics, passes=20, iterations=500, alpha='auto')
    all_topics = lda.get_document_topics(corpus, per_word_topics=True)

    return lda, all_topics, lda.expElogbeta, dictionary

def lda_test(ldaModel, words):
    dictionary = Dictionary().load('documents.dict')
    corpus = [dictionary.doc2bow(text) for text in words]

    all_topics_test = ldaModel.get_document_topics(corpus, per_word_topics=True)

    return all_topics_test


