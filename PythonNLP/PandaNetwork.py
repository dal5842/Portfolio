import spacy
import os
import pandas as pd
import nltk
from nltk.corpus import wordnet as wn

nltk.download('wordnet')
nlp = spacy.cli.download("en_core_web_md")

nlp = spacy.load("en_core_web_md")

collPath = 'PythonNLP'


def wordCollector(words, unit):
    wordList = []
    nodeAtts = []
    synsetCounts = []
    unitList = []
    for token in words:
        if token.pos_ == "ADJ":
            synsets = len(wn.synsets(token.lemma_))
            wordList.append(token.lemma_)
            nodeAtts.append(token.pos_)
            synsetCounts.append(synsets)
            unitList.append(unit)

    data = {
        'word': wordList,
        'nodeType': nodeAtts,
        'synsetCount': synsetCounts,
        'unit': unitList
    }
    df = pd.DataFrame(data)
    return df

allDataFrames = []

for file in os.listdir(collPath):
    if file.endswith(".txt"):
        filepath = f"{collPath}/{file}"
        name, extension = os.path.splitext(file)
        print(name)
        with open(filepath, 'r', encoding='utf8') as f:
            readFile = f.read()
            lengthFile = len(readFile)
            print(lengthFile)
            myDataFrame = wordCollector(spacyRead, name)
            allDataFrames.append(myDataFrame)
            myWords = wordCollector(spacyRead, name)
            print(myWords)
            spacyRead = nlp(readFile)
            for token in spacyRead:
                print(token.text, "---->", token.pos_, ":::::", token.lemma_)

outputFilePath = 'PandaNetworkData.tsv'
fullDataFrame = pd.concat(allDataFrames, ignore_index=True)

fullDataFrame.to_csv(outputFilePath, sep='\t', index=False)

print(f"Saved a NEW dataframe as a NEW TSV file saved to: {outputFilePath}")