import pyexcel
import os
import numpy


def sort_and_save_topics(topics_expElogbeta, dictionary, words, filename):
   topic_count= len(topics_expElogbeta)
   data = [None] * topic_count
   sorted_lists = [None] * topic_count
   for i in range(0, topic_count):
        data[i] = []
        sorted_lists[i] = []
   for i in range(0, topic_count):
       for word in words:
            data[i].append([topics_expElogbeta[i][dictionary.token2id[word]], word])

   for i in range(0, topic_count):
       sorted_lists[i] = sorted(data[i], reverse=True)
       class_file_name=filename+'class'+str(i)+'.csv'
       pyexcel.save_as(array=([['probability','word']]+sorted_lists[i]), dest_file_name=class_file_name)

   return sorted_lists

def cleanup(list):
    for file in list:
        os.remove(file)

def save_word2vec_topics(extended_topics, w2v_output):
   topic_count= len(extended_topics)

   for i in range(0, topic_count):
       class_file_name=w2v_output+'class'+str(i)+'.csv'
       pyexcel.save_as(array=([['basic word', 'probability', 'word form Word2Vec']]+extended_topics[i]), dest_file_name=class_file_name)


def choose_topic(extended_topics, words_in_documents, files_count, topics_count, logger): #files?
    document_topic = [None] * files_count
    for i in range(0, files_count):
        document_topic[i] = [None] * topics_count
        for j in range(0, topics_count):
            document_topic[i][j] = 0

    i = 0
    for words_in_document in words_in_documents:
        logger.info("Choosing topic for document "+str(i)+" of "+str(files_count))
        for word in words_in_document:
            distributions = find_distributions(word, extended_topics, topics_count)
            topic = choose_topic_with_distribution(distributions, topics_count)
            document_topic[i][topic] += 1
        i += 1

    return document_topic


def choose_topic_with_distribution(distributions, topics_count):
    return numpy.random.choice(numpy.arange(0, topics_count), p=distributions)

def find_distributions(word, extended_topics, topics_count):
    distributions = [0.000001,0.000001,0.000001,0.000001,0.000001]
    for i in range(0, topics_count):
        for j in range(0, len(extended_topics[i])):
            if (extended_topics[i][j][2] == word):
                distributions[i] = extended_topics[i][j][1]
    normed = [i / sum(distributions) for i in distributions]
    return normed

def save_and_calculate_topic_document_distribution(files, doc_topic, output_file, topic_count):
    data = []
    for i in range(0, len(doc_topic)):
        values = []
        values.append(files[i])
        sum = 0
        for j in range(0, topic_count):
            sum += doc_topic[i][j]
        for j in range(0, topic_count):
            val = float(doc_topic[i][j]) / sum
            values.append(val)
        data.append(values)

    pyexcel.save_as(array=([['document', 'probabilities']]+data), dest_file_name=output_file)