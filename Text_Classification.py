# Text Classification

# Sentiment analysis

# Consider movie review
# A positive connotation or a negative connotation


import nltk
import random
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)),category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

print(documents[1])



all_words = []
count=0
for w in movie_reviews.words():
    all_words.append(w.lower())
    count+=1
print()
print("All the words in reviews would amount to : " + str(count))


all_words = nltk.FreqDist(all_words)
print(all_words.most_common(15))
print(all_words["amazing"])
