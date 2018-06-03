# Stemming and lemetization
# Example:
#       I was taking a ride in the car vs
#       I was riding the car

# Porter stemmer

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps=PorterStemmer()
example_word = ["python","pythoner","pythoning","pythoned","pythonly"]

##for w in example_word:
##    print(ps.stem(w))
##

new_text = "it is very important for python to pythonly pythonify the pythoner job of pythoning"
words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w))
