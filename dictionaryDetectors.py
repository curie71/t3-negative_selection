import sys
import glob
import re
import os

def keepWords(word, list):
    removed = re.sub("[(),/]", '', word).strip('[]')
   
    if len(list) == 0:
        list.append(removed)
 
    for item in list:
        if removed not in list:
            list.append(removed)    

def saveWords(list):
    count = 0
    n = 0

    file = open('detector_words.txt', 'w+')
    for word in list:
        file.write("%s\n" % word)        

try:
    path = sys.argv[1]
    list = []
    for filename in glob.glob(os.path.join(path, '*.txt')):
        with open(filename, "r") as fo:
            for line in fo:
                for word in line.split():
                    if len(word) > 1:
                        keepWords(word, list)
            saveWords(list) 
        fo.close()
    print "Arquivo com os detectores gerados com sucesso"

except:
    print('Passe um diretorio')