import urllib.request
import re

#This function reads the input file from the file and replaces all newline characters with a space
def read_text():
 quotes=open('C:\Python34\movie.txt')
 file_content=quotes.read()
 file_new_content=re.sub('\n', ' ',file_content)
 print(file_new_content)
 quotes.close()
 profanity_check(file_new_content)
 
 #Profanity checking function which uses wdyl profanity checker and spits out true
 # if the input file contains profanity words and false otherwise
def profanity_check(text_to_check):
 file_new_content=re.sub(' +', '%20',text_to_check)
 response=urllib.request.urlopen("http://www.wdyl.com/profanity?q="+file_new_content)
 output=response.read()
 print(output)
