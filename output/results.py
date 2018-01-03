import pyexcel
import os


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
       pyexcel.save_as(array=([['basic word','word form Word2Vec']]+extended_topics[i]), dest_file_name=class_file_name)