import os
import re


whereTrain = '/Users/magdalenas/Downloads/webkb2/train/'
whereTest = '/Users/magdalenas/Downloads/webkb2/test/'

def getFilenames(isTrain = True):
    i = 0
    if (isTrain):
        filesPath = whereTrain
    else:
        filesPath = whereTest
    castFiles = []
    for path, dnames, fnames in os.walk(filesPath):
        castFiles.extend([os.path.join(path, x) for x in fnames if not x[0] == '.'])
    return castFiles