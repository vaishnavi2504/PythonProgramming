import urllib.request
import re

def read_text():
 quotes=open('C:\Python34\movie.txt')
 file_content=quotes.read()
 file_new_content=re.sub('\n', ' ',file_content)
 print(file_new_content)
 quotes.close()
 profanity_check(file_new_content)
 
def profanity_check(text_to_check):
 file_new_content=re.sub(' +', '%20',text_to_check)
 response=urllib.request.urlopen("http://www.wdyl.com/profanity?q="+file_new_content)
 output=response.read()
 print(output)
