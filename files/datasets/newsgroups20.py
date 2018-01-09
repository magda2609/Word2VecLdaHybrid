import os
import re


where = '/Users/magdalenas/Downloads/20news-bydate/20news-bydate-train/'

def getFilenames():
    castFiles = []
    for path, dnames, fnames in os.walk(where):
        castFiles.extend([os.path.join(path, x) for x in fnames if not x[0] == '.'])
    return castFiles