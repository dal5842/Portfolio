import spacy
import pandas as pd
import os
import nltk
from nltk.corpus import wordnet as wn

# Load spaCy language model
nlp = spacy.load("en_core_web_md")

# Set path to your cleaned project text files
collPath = '../PythonNLP'  # <-- change this to your actual folder name

# Define the word collection function
def wordCollector(words, unit):
    wordList = []
    nodeAtts = []
    synsetCounts = []
    unitList = []

    for token in words:
        if token.pos_ == "ADJ":
            lemma = token.lemma_
            synsets = len(wn.synsets(lemma))
            wordList.append(lemma)
            nodeAtts.append(token.pos_)
            synsetCounts.append(synsets)
            unitList.append(unit)

    data = {
        'word': wordList,
        'nodeType': nodeAtts,
        'synsetCount': synsetCounts,
        'unit': unitList
    }

    return pd.DataFrame(data)

# Process all files and collect data
allDataFrames = []

for file in os.listdir(collPath):
    if file.endswith(".txt"):
        filepath = os.path.join(collPath, file)
        name, _ = os.path.splitext(file)

        with open(filepath, 'r', encoding='utf8') as f:
            readFile = f.read()
            spacyRead = nlp(readFile)
            df = wordCollector(spacyRead, name)
            allDataFrames.append(df)

# Combine all DataFrames into one
fullDataFrame = pd.concat(allDataFrames, ignore_index=True)

# Create the output folder if it doesn't exist
outputDir = os.path.join(collPath, "output")
os.makedirs(outputDir, exist_ok=True)

# Save as TSV for Cytoscape
outputPath = os.path.join(outputDir, "PandaNetworkData.tsv")
fullDataFrame.to_csv(outputPath, sep='\t', index=False)

print(f"✅ TSV saved to: {outputPath}")