from files.datasets import fifteenTypes, newsgroups20

LOG_LEVEL = "INFO"
LOG_FILE = "./output/logging.log"

filename_types = fifteenTypes
folder = './output/fifteenTypes'

#train
topics = 6
number_of_extended_words = 100
w2v_similarity = 0.45
lda_doc_results = folder+'/train_lda_doc_results.csv'
lda_output = folder+'/train_lda_word_results'
w2v_output = folder+'/train_w2v_results'
all_output_choosen = folder+'/train_all_results_choosen.csv'
all_output_max = folder+'/train_all_results_max.csv'

#test
all_output_choosen_test = folder+'/test_all_results_choosen.csv'
all_output_max_test = folder+'/test_all_results_max.csv'
lda_doc_results_test = folder+'/test_lda_doc_results.csv'
