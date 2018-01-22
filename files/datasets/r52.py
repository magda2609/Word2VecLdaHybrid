import os
import re


whereTrain = './files/datasets/data/r52/train/r52-train-all-terms.txt'
whereTest = './files/datasets/data/r52/test/r52-test-all-terms.txt'

def getFilenames(isTrain = True):
    if (isTrain):
        filesPath = whereTrain
    else:
        filesPath = whereTest
    files, text = loadFilenameWithSentences(filesPath)
    return files, text

def loadFilenameWithSentences(fileName):
    text = []
    i = 1
    files = []
    with open(fileName, 'r') as infile:
        lines = infile.readlines()
        for line in lines:
            vals = line.split('\t')
            text.append(vals[1])
            files.append(vals[0]+str(i))
            i = i+1
    return files, text
