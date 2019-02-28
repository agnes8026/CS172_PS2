#-*- coding:utf-8 -*-

import sys
import pickle					
from nltk import *																							#import natural-language-toolkit
from operator import itemgetter																	#for sort


STOPWORDS = []																							#grobal variable

def output_index(result):
	#print result

	output = open('data.pkl', 'wb')
	pickle.dump(result, output)																		# Pickle dictionary using protocol 0
	output.close()


def pre_file(filename): 
	global STOPWORDS
#	print("read file %s.txt....."%filename) 															#show process
	content = open( str(filename) + '.txt', "r").read()
	content = content.lower()
	for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_¡®{|}~' :											#cancel the punction
		content = content.replace(ch, " ")
	
	for ch in  STOPWORDS:																				#cancel the stopwords
		content = content.replace(ch, " ")		

	plurals = content.split()																				#split the file at '\n' or ' '

	stemmer = PorterStemmer()																		#prepare for stemming
	singles = [stemmer.stem(plural) for plural in plurals]									#handling stemming

	return singles

def readfile(filename):  
	input = open(filename, 'r')																		#titles that need to be handled
	all_the_file =input.read( )
	words = all_the_file.split()																			#split the file at '\n' or ' '
	input.close()			
	return words



#main function
def main(): 
	global STOPWORDS
	print "read index....."																					#show process
	file=readfile('index.txt')
	print "read stopwords....."	
	STOPWORDS = readfile('data/stoplist.txt')  

	print "create word list....."
	word = list(readfile('wordfile.txt'))																		#the file with all the words in all the books
	result = {}																										#memorize the result 

	for x in range( 0, len(file) ):
		#print file[x]
		
		txt = pre_file( file[x] )
		txt =  {}.fromkeys(txt).keys()	
		#can also use text.set()															

		for words in txt :
			words =words.decode('utf-8').encode(sys.getfilesystemencoding())
			if result.get(words) == None :
				result[words]=[file[x]]
			else:
				t=result.get(words)
				t.append(file[x])
				result[words]=t

	
	output_index(result)
	

		
#runfile
if __name__ == '__main__': 
    main() 
    
pass  # NOQA    