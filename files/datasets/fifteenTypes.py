where = '/Users/magdalenas/Downloads/TextMIning/untitledfolder/'

fileNames = [
    'animal1.txt',
    'animal2.txt',
    'animal3.txt',
    'art1.txt',
    'art2.txt',
    'art3.txt',
    'science1.txt',
    'science2.txt',
    'science3.txt',
    'sport1.txt',
    'sport2.txt',
    'sport3.txt',
    'travel1.txt',
    'travel2.txt',
    'travel3.txt'

]

def getFilenames():
    castFiles = []
    for fileName in fileNames:
        castFiles.append(where + fileName)
    return castFiles

def getDocumentsCount():
    return 15