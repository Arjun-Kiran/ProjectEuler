# Project Euler Problem 22
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
# What is the total of all the name scores in the file?
import math,sys,os


def alphabetScore(sLetter):
	score = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
	sLetter = sLetter.lower()
	return score.get(sLetter)

def wordScore(sWord):
	score = 0
	for i in sWord:
		score += alphabetScore(i)
	return score

def scoreArray(arrayScores):
	#arrayScores.sort()
	print arrayScores[937]
	print arrayScores[938]
	rank = 0
	score = 0
	for i in arrayScores:
		rank += 1
		score += i*rank 
	return score

def main(lineArray):
	rankArray = []
	lineArray.sort()
	for item in lineArray:
		item = item.replace('\"','')
		rankArray.append(wordScore(item))
	print scoreArray(rankArray)

#testArray = [123,23,58,90]

#print scoreArray(testArray)
if len(sys.argv) < 2:
	print "NEED A FILENAME"
else:
	FILENAME = sys.argv[1]
	fObject = open(FILENAME,'r')
	LINE = fObject.readline()
	fObject.close()
	nameArray = LINE.split(',')
	main(nameArray)

