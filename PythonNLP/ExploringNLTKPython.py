import nltk
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize

# Load the text file
with open("GDWake.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Tokenize words
words = word_tokenize(text)

# Calculate frequency distribution
freq_dist = FreqDist(words)

# Print some basic text analysis
print("Total words:", len(words))
print("Unique words:", len(set(words)))
print("Most common words:", freq_dist.most_common(10))