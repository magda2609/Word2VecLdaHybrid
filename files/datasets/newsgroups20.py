import os
import re


whereTrain = './files/datasets/data/20news-bydate-train/'
whereTest = './files/datasets/data/20news-bydate-test/'

def getFilenames(isTrain = True):
    if (isTrain):
        filesPath = whereTrain
    else:
        filesPath = whereTest
    castFiles = []
    for path, dnames, fnames in os.walk(filesPath):
        castFiles.extend([os.path.join(path, x) for x in fnames if not x[0] == '.'])
    return castFiles
