from nltk.corpus import wordnet

syns = wordnet.synsets("good")
print(syns)
print()

print(syns[0].lemmas())
print()

print("*************")
print(syns[0].lemmas()[0].name())
print()

print("This is what comes out as the defination:")
print(syns[0].definition())
print()

print("The examples to use good are")
print(syns[0].examples())
print()

print("Lets take a look at the antonyms")
print(syns[1].lemmas()[0].antonyms())
print("------------------------------------------")


synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):    
    for l in syn.lemmas():
        synonyms.append(l.name())
        print(l)
        if l.antonyms():
            #print("This has an antonym " + str(l))
            antonyms.append(l.antonyms()[0].name())
print(set(synonyms))
print(set(antonyms))



## Semantic Similarity
##
##w1 = wordnet.synset("ship.n.01")
##w2 = wordnet.synset("boat.n.01")
##
##print("The similarity between words w1 and w2")
##print(str(w1.wup_similarity(w2) * 100) + " percent")



w3 = wordnet.synsets("ship")[0]
w4 = wordnet.synsets("boat")[0]


print()
print(w3)
print(w4)
print(str(w3.wup_similarity(w4) * 100) + " percent")
    
