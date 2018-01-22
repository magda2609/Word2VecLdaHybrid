import os
import re


whereTrain = '/Users/magdalenas/Downloads/webkb2/train/'
whereTest = '/Users/magdalenas/Downloads/webkb2/test/'

def getFilenames(isTrain = True):
    if (isTrain):
        filesPath = whereTrain
    else:
        filesPath = whereTest
    castFiles = []
    castFiles = load(filesPath, castFiles)
    return castFiles

def load(where, castFiles):
    for path, dnames, fnames in os.walk(where):
        for dict in dnames:
            castFiles = load(str(path)+str(dict)+'/', castFiles)
        # castFiles[2][len(castFiles[2]) - 5:] == '.html'
        castFiles.extend([os.path.join(path, x) for x in fnames if not x[0] == '.' and x[len(x) - 5:] == '.html'])
    return castFiles