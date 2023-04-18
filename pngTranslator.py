#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 10:11:49 2021

@author: hack-rafa
"""

from zipfile import ZipFile


inputFile = '571587_1_1.pgn'
outputFile = '1aRodadaBrasileiroAbsoluto2021.pgn'
outputZipFile = '1aRodadaBrasileiroAbsoluto2021.pgn.zip'


with open(inputFile, 'r') as f:
    pgnText = f.read()

pgnTextTranslated = ""
for i in range(len(pgnText.split("\n"))):
    linha = pgnText.split("\n")[i]
    if "[" not in linha:
        linha = linha.replace("C", "N")
        linha = linha.replace("D", "Q")
        linha = linha.replace("R", "K")
        linha = linha.replace("T", "R")
        print(linha)
    pgnTextTranslated += linha
    pgnTextTranslated += "\n"
    

with open(outputFile, 'w') as f:
    f.write(pgnTextTranslated)


# create a ZipFile object
zipObj = ZipFile(outputZipFile, 'w')
# Add multiple files to the zip
zipObj.write(outputFile)
# close the Zip File
zipObj.close()


