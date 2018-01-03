from files.word2vec import getModelDirectory
from gensim.models.word2vec import Word2Vec

def w2v_extend_topics(topics, number_of_words, w2v_similarity, logger):
   topic_count= len(topics)
   newTopics = [None] * topic_count
   logger.info("Reading Word2Vec model")
   model = readModel()

   logger.info("Extending results")
   for i in range(0, topic_count):
        newTopics[i] = []
        for j in range(0, number_of_words):
            word_topic = topics[i][j]
            words = get_similar_words(model, word_topic[1], w2v_similarity)
            if  (len(words) > 0):
                newTopics[i].extend(words)

   return newTopics


def readModel():
    return Word2Vec.load_word2vec_format(getModelDirectory(), binary=True)

def get_similar_words(model, word, w2v_similarity):
    words = []
    try:
        all_words = model.similar_by_vector(model[word], topn=200)
        for i in all_words:
            if (i[1] >= w2v_similarity):
                words.append([word, i[0]])
            else:
                return words
        return words
    except KeyError:
        return words