# Figure out the meaning
# Parts of speech tagging

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer


train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)
##print(train_text)
##print()
##print(sample_text)
##print()

print(tokenized)
def process_context():
    try:
        for i in tokenized:
            words=nltk.word_tokenize(i)
            tagged=nltk.pos_tag(words)
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>} """
##            print(tagged)
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
##            print(chunked)
            chunked.draw()
    except Exception as e:
        print(str(e))

process_context()
