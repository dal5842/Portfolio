import spacy
import os

nlp = spacy.load('en_core_web_md')

word_of_interest_text = 'dream'
word_of_interest = nlp(word_of_interest_text)

collPath = '../PythonNLP'
print("Collection path: " + collPath)

all_similar_words = {}

def readTextFiles(filepath, filename):
    with open(filepath, 'r', encoding='utf8') as f:
        text = f.read()
        doc = nlp(text)

        high_similarity = {}

        for token in doc:
            if token.has_vector and not token.is_stop and not token.is_punct:
                sim_score = word_of_interest.similarity(token)
                if sim_score > 0.3 and token.text.lower() != word_of_interest_text.lower():
                    high_similarity[token.text] = sim_score

        sorted_similarity = dict(sorted(high_similarity.items(), key=lambda item: item[1], reverse=True))

        print(f"\nTop similar words in {filename}:")
        for word, score in list(sorted_similarity.items())[:10]:
            print(f"{word}: {score:.3f}")

        all_similar_words[filename] = sorted_similarity

for file in os.listdir(collPath):
    if file.endswith(".txt"):
        filepath = os.path.join(collPath, file)
        name, _ = os.path.splitext(file)

        with open(filepath, 'r', encoding='utf8') as f:
            readFile = f.read()
            spacyRead = nlp(readFile)

print("\n\nSummary Across All Files:")
for filename, word_dict in all_similar_words.items():
    print(f"\nFile: {filename}")
    for word, score in list(word_dict.items())[:5]:
        print(f"  {word}: {score:.3f}")