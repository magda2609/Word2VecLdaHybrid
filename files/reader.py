from gensim.utils import smart_open
from gensim.corpora.wikicorpus import _extract_pages, filter_wiki
from gensim.corpora import Dictionary


def read_files(filename_types):
    files = []
    for fileName in filename_types.getFilenames():
        with open(fileName, 'r') as infile:
            files.append(infile.readlines())
    return files

def read_wiki_files():
    return iter_wiki('/Users/magdalenas/Downloads/simplewiki-latest-pages-articles.xml.bz2')

def iter_wiki(dump_file):
    files = []
    file = []
    last_title = ''
    for title, text, pageid in _extract_pages(smart_open(dump_file)):
        text = filter_wiki(text)
        file.append(text)
        if last_title != title:
            files.append(file)
            file = []
        last_title = title

    return files