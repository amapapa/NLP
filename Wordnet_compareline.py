##############################################################################################
##############################################################################################
#
#-------------   Module to compare semantix similarity of text file for a delta difference
#   ----------   Implemented Semantic match using simple WORDNET from NLTK
#        -----   FURTHER USECASE ON "LATENT SEMANTIC ANALYSIS"
#
#
###############  AUTHOR   :  AMARENDRA MAHAPATRA
###############  DATE     :  04-23-2018
#
##############################################################################################
##############################################################################################


import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize,sent_tokenize





###############################################
## Compare words using nltk wordnet for a starter
## Later I can look into semantic comparision  using LSA
###############################################

def compare_words(text1,text2):
    syn1 = wordnet.synsets(str(text1))
    syn2 = wordnet.synsets(str(text2))

##    print(syn1)
##    print(syn2)
    text2_syns=[]

    for i in syn2:
        for l in i.lemmas():
            text2_syns.append(l.name())

    print(type(text2_syns))
    match_found = "False"    
    for word in text2_syns:
        if word == text1:
            print(word + " match? " + text1)
            match_found = "True"
        return(match_found)


##############################################
#   End of function
##############################################

def match_lines(left_line,right_line):
    
    line1 = left_line 
    line2 = right_line


    print("Line 1 :" + line1)
    print("Line 2 :" + line2)

    ###############################################
    # count the number of words in each line
    ###############################################

    print("Tokenize line1 " +str(word_tokenize(line1)))
    print("Tokenize line2 " +str(word_tokenize(line2)))


    ###############################################
    # get the length
    ###############################################
    line1_tok = word_tokenize(line1)
    line2_tok = word_tokenize(line2)

    print()
    print(len(line1_tok))
    print(len(line2_tok))

    ###############################################
    #  lets see the difference
    ###############################################

    if len(line1_tok) == len(line2_tok):
        for i in range(len(line1_tok)):
            if line1_tok[i]!=line2_tok[i]:
                
            ##  compare_words
                lines_match="False"
                test = compare_words(line1_tok[i],line2_tok[i])
                if test:
                    print("The text matches")
                    lines_match="True"
                else:
                    print("sentences don't match")
    return(lines_match)

        
