#This program is used for simple spell check 
#spellCheck.txt is present in the same folder as that of the python pgm

words=open("spellCheck.txt").readlines()

#The strip function is needed to remove the newline character at the end of each word.
words = map(lambda x: x.strip(), words)
print('zygoti' in words)
