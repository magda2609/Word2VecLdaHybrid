import settings
from files.remove_list import get_list
from files.reader import read_files
from files.reader import read_wiki_files
from words.cleaner import tokenize, unique_words
from output.results import sort_and_save_topics, cleanup, save_word2vec_topics
from lda.lda import lda
from w2v.w2v import w2v_extend_topics
import nltk
from logger import Logger


logger = Logger().get_logger("LDA_Word2Vec_hybrid")

logger.info("Reading files")
# files = read_files(filename_types = settings.filename_types)
files = read_wiki_files()

logger.info("Tokenization process")
words_in_documents = tokenize(files)
logger.info("Unique words")
unique_words = unique_words(words_in_documents)
logger.info("LDA")
topics_expElogbeta, dictionary = lda(words_in_documents, settings.topics)
logger.info("Saving LDA results")
sorted_topics = sort_and_save_topics(topics_expElogbeta, dictionary, unique_words, settings.lda_output)
logger.info("Extending results by Word 2 Vec")
extended_topics = w2v_extend_topics(sorted_topics, settings.number_of_extended_words, settings.w2v_similarity, logger)
logger.info("Saving W2V results")
save_word2vec_topics(extended_topics, settings.w2v_output)
logger.info("Cleaning up")
cleanup(get_list())
logger.info("Finished!!")
