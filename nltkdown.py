
# tokenize  - word tokenizers and sentence tokenizer
# lexicon and corpora -
# Corpora : body of text :  medical journal, examples of presidential speeches
# Lexicon : Dicionary  :: Words and meanings
# investor-speak vs regular english
# Investor speaks 'bull'  vs regular english "bull: animal"


from nltk.tokenize import sent_tokenize, word_tokenize

example_text ="Hello Mr. Smith, how are you doing today? The weather is great and python is awesome. The sky is pinkish blue and you are awesome"
print(sent_tokenize(example_text))
print(word_tokenize(example_text))
