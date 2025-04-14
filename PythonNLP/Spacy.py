import spacy
import nltk
from collections import Counter
from nltk.corpus import wordnet as wn

nltk.download('wordnet')

nlp = spacy.load("en_core_web_lg")

file = open("dracula.xml", "r", encoding="utf-8")
text = file.read()
file.close()

doc = nlp(text)

def collect_verbs(doc):
    verbs = []
    for token in doc:
        if token.pos_ == "VERB":
            verbs.append(token.lemma_)
    return verbs

verb_list = collect_verbs(doc)

verb_freq = Counter(verb_list)

output = open("SpacyVerbFreq.txt", "w", encoding="utf-8")
for item in verb_freq.most_common():
    output.write(str(item) + "\n")
output.close()

unique_verbs = sorted(set(verb_list))
for word in unique_verbs[:20]:
    syns = wn.synsets(word)
    print(f"'{word}' belongs to {len(syns)} synsets in WordNet.")
    print("Processing file:", file)
    print("Top 20 verbs:", verb_freq.most_common(20))