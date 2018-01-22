import settings
from files.remove_list import get_list
from files.reader import read_files
from files.reader import read_wiki_files
from words.cleaner import tokenize, unique_words
from output.results import sort_and_save_topics, cleanup, save_word2vec_topics, choose_topic, save_and_calculate_topic_document_distribution, save_lda_document_distributions
from lda.lda import lda, lda_test
from w2v.w2v import w2v_extend_topics
import nltk
from logger import Logger


nltk.download("wordnet")
nltk.download("stopwords")

logger = Logger().get_logger("LDA_Word2Vec_hybrid")

logger.info("Reading files")
filenames_train = settings.filename_types.getFilenames(isTrain=True)
files = read_files(filenames = filenames_train)
# files = read_wiki_files()
logger.info(str(len(files))+" files found")

logger.info("Tokenization process")
words_in_documents = tokenize(files, logger)
logger.info(str(len(words_in_documents))+" words found")
logger.info("Unique words")
unique_words = unique_words(words_in_documents)
logger.info(str(len(unique_words))+" unique words found")
logger.info("LDA")
lda, all_topics, topics_expElogbeta, dictionary = lda(words=words_in_documents, topics=settings.topics)
logger.info("Saving LDA results")
save_lda_document_distributions(all_topics, filenames_train, settings.lda_doc_results)
sorted_topics = sort_and_save_topics(topics_expElogbeta, dictionary, unique_words, settings.lda_output)
logger.info("Extending results by Word 2 Vec")
extended_topics = w2v_extend_topics(sorted_topics, settings.number_of_extended_words, settings.w2v_similarity, logger)
logger.info("Saving W2V results")
save_word2vec_topics(extended_topics, settings.w2v_output)

logger.info("Verifying:")
logger.info("Choosing topics")
doc_topic_choosen, doc_topic_max = choose_topic(extended_topics, words_in_documents, len(files), settings.topics, logger)
logger.info("Saving document_topics_distributions:")
save_and_calculate_topic_document_distribution(filenames_train, doc_topic_choosen, settings.all_output_choosen, settings.topics)
save_and_calculate_topic_document_distribution(filenames_train, doc_topic_max, settings.all_output_max, settings.topics)



logger.info("Time to test")
logger.info("Reading files")
filenames_test = settings.filename_types.getFilenames(isTrain=False)
files_test = read_files(filenames = filenames_test)
logger.info("Tokenization process")
words_in_documents_test = tokenize(files_test, logger)
logger.info(str(len(words_in_documents_test))+" words found")
all_topics_test = lda_test(lda, words_in_documents_test)
save_lda_document_distributions(all_topics_test, filenames_test, settings.lda_doc_results_test)

doc_topic_choosen_test, doc_topic_max_test = choose_topic(extended_topics, words_in_documents_test, len(files_test), settings.topics, logger)
logger.info("Saving document_topics_distributions:")
save_and_calculate_topic_document_distribution(filenames_test, doc_topic_choosen_test, settings.all_output_choosen_test, settings.topics)
save_and_calculate_topic_document_distribution(filenames_test, doc_topic_max_test, settings.all_output_max_test, settings.topics)


logger.info("Cleaning up")
cleanup(get_list())
logger.info("Finished learning!!")
