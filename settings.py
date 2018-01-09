from files.datasets import fifteenTypes, newsgroups20

LOG_LEVEL = "INFO"
LOG_FILE = "./output/logging.log"

filename_types = newsgroups20
topics = 6
number_of_extended_words = 100
w2v_similarity = 0.45
lda_output = './output/20_newsgroups2/lda_results'
w2v_output = './output/20_newsgroups2/w2v_results'
all_output = './output/20_newsgroups2/all_results.csv'