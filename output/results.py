import pyexcel
import os
import numpy
from operator import itemgetter


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
    myDict = [None] * topics_count
    for i in range(0, topics_count):
        myDict[i] = {}
        for j in range(0, len(extended_topics[i])):
            myDict[i][extended_topics[i][j][2]] = extended_topics[i][j][1]

    document_topic_choosen = [None] * files_count
    document_topic_max = [None] * files_count
    for i in range(0, files_count):
        document_topic_choosen[i] = [None] * topics_count
        document_topic_max[i] = [None] * topics_count
        for j in range(0, topics_count):
            document_topic_choosen[i][j] = 0
            document_topic_max[i][j] = 0

    i = 0
    for words_in_document in words_in_documents:
        logger.info("Choosing topic for document "+str(i)+" of "+str(files_count))
        for word in words_in_document:
            distributions = find_distributions(word, myDict, topics_count)
            topic = choose_topic_with_distribution(distributions, topics_count)
            document_topic_choosen[i][topic] += 1
            document_topic_max[i][distributions.index(max(distributions))] += 1
        i += 1

    return document_topic_choosen, document_topic_max


def choose_topic_with_distribution(distributions, topics_count):
    return numpy.random.choice(numpy.arange(0, topics_count), p=distributions)

def find_distributions(word, myDict, topics_count):
    distributions = []
    for i in range(0, topics_count):
        distributions.append(0.000001)
    for i in range(0, topics_count):
        if (myDict[i].get(word,None) is not  None):
            distributions[i] = myDict[i][word]
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
        values.append(values.index(max(values[1:])))
        data.append(values)

    pyexcel.save_as(array=([['document', 'probabilities', 'topic']]+data), dest_file_name=output_file)

def save_lda_document_distributions(all_topics, filenames, output_file):
    data = []
    i = 0
    for all_docs in all_topics:
        for doc_topics in all_docs[1]:
            if (len(doc_topics) > 2):
                newList = numpy.array(doc_topics)
                print newList
                data.append([filenames[i], (max(newList, key=itemgetter(1)))[0]])
            elif (len(doc_topics) == 1):
                data.append([filenames[i], doc_topics[0][0]])
            i = i+1

    pyexcel.save_as(array=([['document', 'topic']]+data), dest_file_name=output_file)
