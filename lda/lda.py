from gensim.models.ldamodel import LdaModel
from gensim.corpora import Dictionary, MmCorpus
from gensim.utils import ClippedCorpus

def lda(words, topics):
    dictionary = Dictionary(words)
    dictionary.save('documents.dict')
    corpus = [dictionary.doc2bow(text) for text in words]
    MmCorpus.serialize('documents.mm', corpus)
    mm_corpus = MmCorpus('documents.mm')

    mm = ClippedCorpus(mm_corpus, 4000)

    lda = LdaModel(corpus=mm, id2word=dictionary, num_topics=topics, passes=10, iterations=1000)

    return lda.expElogbeta, dictionary