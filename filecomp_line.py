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

# Ref code for file comparision from : https://www.guru99.com/reading-and-writing-files-in-python.html


import Wordnet_compareline


f1 = open("C:\\Users\\a502504\\Python\\File1.txt","r")
f2 = open("C:\\Users\\a502504\\Python\\File2.txt","r")

# Print confirmation
print("-----------------------------------")
print("Comparing files ", " > " + "f1", " < " +"f2", sep='\n')
print("-----------------------------------")

# Read the first line from the files
f1_line = f1.readline()
f2_line = f2.readline()

# Initialize counter for line number
line_no = 1

# Loop if either file1 or file2 has not reached EOF
while f1_line != '' or f2_line != '':

    # Strip the leading whitespaces
    f1_line = f1_line.rstrip()
    f2_line = f2_line.rstrip()
    
    # Compare the lines from both file
    if f1_line != f2_line:
        
        # If a line does not exist on file2 then mark the output with + sign
        if f2_line == '' and f1_line != '':
            print(">+", "Line-%d" % line_no, f1_line)
        # otherwise output the line on file1 and mark it with > sign
        elif f1_line != '':
            print(">", "Line-%d" % line_no, f1_line)
            
        # If a line does not exist on file1 then mark the output with + sign
        if f1_line == '' and f2_line != '':
            print("<+", "Line-%d" % line_no, f2_line)
        # otherwise output the line on file2 and mark it with < sign
        elif f2_line != '':
            print("<", "Line-%d" %  line_no, f2_line)

        # Print a blank line
        print()
        if f1_line != '' and f2_line != '':
            semantic_similarity = Wordnet_compareline.match_lines(f1_line,f2_line)
            print(semantic_similarity)
            
    #Read the next line from the file
    f1_line = f1.readline()
    f2_line = f2.readline()


    #Increment line counter
    line_no += 1

# Close the files
f1.close()
f2.close()

