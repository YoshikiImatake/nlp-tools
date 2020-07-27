import os, sys, shutil, MeCab
m = MeCab.Tagger ("-r C:\progra~2\MeCab\etc\mecabrc-u")

inDir = 'text/'
outDir = 'text_mcb/'
fileName = 'sample.txt'


path = inDir + fileName
path_mcb = outDir + fileName.replace('.txt', '_mcb.txt')
with open(path, mode='r', encoding='utf-8') as file:
    with open(path_mcb, mode='w', encoding='utf-8') as file_mcb:
        for row in file:
            file_mcb.write(m.parse (row))
