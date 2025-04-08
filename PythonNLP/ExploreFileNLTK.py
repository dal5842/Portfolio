import nltk.corpus
nltk.download('book')
from nltk.book import *
import matplotlib.pyplot as plt

# Load text file
with open("GDWake.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Tokenize
tokens = word_tokenize(text)
text_nltk = nltk.Text(tokens)

print(f"Total words: {len(tokens)}")
print(f"Unique words: {len(set(tokens))}")

# Frequency Distribution
fdist = FreqDist(w.lower() for w in tokens if w.isalpha() and len(w) > 4)

# Plot
fdist.plot(30, cumulative=False)
plt.show()

text_nltk.concordance("wake")