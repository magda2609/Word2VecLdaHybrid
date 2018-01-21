import os
import re


whereTrain = '/Users/magdalenas/Downloads/20news-bydate/20news-bydate-train/'
whereTest = '/Users/magdalenas/Downloads/20news-bydate/20news-bydate-test/'

def getFilenames(isTrain = True):
    if (isTrain):
        filesPath = whereTrain
    else:
        filesPath = whereTest
    castFiles = []
    for path, dnames, fnames in os.walk(filesPath):
        castFiles.extend([os.path.join(path, x) for x in fnames if not x[0] == '.'])
    return castFiles