#Claire Cahoon
#2017-18 Thesis Project

from __future__ import division
import re
from textblob import TextBlob
from textblob import Word


class LiteraryAnalyzer:
    '''Sets up the textBlob and provides data about it'''
    def __init__(self, theBlob):
        #Bringing in the Blob
        self.theBlob = theBlob
        self.plainWords = ""
        self.sentBlob = theBlob.sentences
        self.wordBlob = theBlob.words

        #default values
        self.numSentences = 0
        self.numWords = 0
        self.avgWordLength = 0
        self.avgWordsPerSent = 0
        self.uniqueWords = 0
        self.wrongCount = 0
        
        self.questCount = 0
        self.exclCount = 0
        self.dashCount = 0
        
        #Parts of Speech
        self.nounCount = 0
        self.nounPerc = 0
        
        self.verbCount = 0
        self.verbPerc = 0
        
        self.adCount = 0
        self.adPerc = 0
        
        self.proCount = 0
        self.proPerc = 0

        #Word List
        self.words = {}
        self.tooCommon = ["a", "an", "the"]

    def getWords(self):
    	'''Returns the full list of words'''
        return self.wordBlob
     
    def fixWords(self):
    	'''Correct contraction errors - alters words in word list to include entire contraction without apostrophe'''
    	#Loop through words
    	for aWord in self.wordBlob:
    		#If index starts with ' or is the second half of a contraction
    		if aWord.startswith("\'") or aWord == "n't":
    			#Find index of original word
    			addInx = (self.wordBlob.index(aWord))-1
    			#Original word
    			addWord = self.wordBlob[addInx]
    			
    			#Concatenate both halves of the word
    			addWord = addWord + aWord
    			
    			#Add word to the end of the list
    			self.wordBlob.append(addWord)
    			#Cut the list around the two old words to remove them
    			self.wordBlob = self.wordBlob[:addInx] + self.wordBlob[addInx+2:]
    			
    	#Create global variable
    	global allWords
    	allWords = self.wordBlob


    def partOfSpeech(self):
        '''Counts the different parts of speech and gives a percentage for how many of that POS are in the text'''
        #Split into Parts of Speech tags
        POS = self.theBlob.tags
        
        #For each item in the list
        for i in range(0, len(POS)):
        
        	#Nouns:
        	if POS[i][1] == "NN" or POS[i][1] == "NNS" or POS[i][1] == "NNP" or POS[i][1] == "NNPS":
        		self.nounCount += 1
        	#Verbs:
        	elif POS[i][1] == "VB" or POS[i][1] == "VBZ" or POS[i][1] == "VBP" or POS[i][1] == "VBD" or POS[i][1] == "VBN" or POS[i][1] == "VBG":
        		self.verbCount += 1
        	#Adjective and Adverbs:
        	elif POS[i][1] == "JJ" or POS[i][1] == "JJR" or POS[i][1] == "JJS" or POS[i][1] == "RB" or POS[i][1] == "RBR" or POS[i][1] == "RBS" or POS[i][1] == "RP":
        		self.adCount += 1
        	#Pronouns:
        	elif POS[i][1] == "PRP" or POS[i][1] == "PSP$":
        		self.proCount += 1
        
        #print(POS[0][1]=="DT")
        
        #Calculate percentage and assign to var
        nounCalc = (self.nounCount/self.numWords)*100
        self.nounPerc = round(nounCalc, 2)
        
        verbCalc = (self.verbCount/self.numWords)*100
        self.verbPerc = round(verbCalc, 2)
        
        adCalc = self.adCount/self.numWords
        self.adPerc = round(adCalc, 2)
        
        proCalc = self.proCount/self.numWords
        self.proPerc = round(proCalc, 2)


    def countWords(self):
        '''Counts the number of total words'''
        for word in self.wordBlob:
            self.numWords += 1

    def countSentences(self):
        '''Counts the number of total sentences'''
        for sent in self.sentBlob:
            self.numSentences += 1
            
    def wordLength(self):
        '''Caclulates average word length'''
        #total number of characters
        totalLen = 0
        
        #Loop through each word in the blob
        for aWord in self.wordBlob:
            #Loop through each character in the word
            for char in aWord:
                #For each, increase the character count
                totalLen += 1

        #Calculate average and assign to global variable
        avrLen = totalLen/self.numWords
        self.avgWordLength = round(avrLen, 2)
            
    def sentLength(self):
        '''Caclulates average sentence length'''
        avrLen = self.numWords/self.numSentences
        self.avgWordsPerSent = round(avrLen, 2)

    def punc(self):
        '''Counts exclamation points and question marks'''
        for aSent in self.sentBlob:
            for aChar in aSent:
            	
                if aChar == "!":
                    self.exclCount += 1
                elif aChar == "?":
                    self.questCount += 1
                elif aChar == "-":
                    self.dashCount += 1
                    
        
    def analyzeBlob(self):
    	self.fixWords()
        self.countWords()
        self.countSentences()
        self.wordLength()
        self.sentLength()
        self.punc()
        self.partOfSpeech()

    def getInfo(self):
    
        info = "\nSentences and Words:"
        info += "\n Number of total sentences: \t" + str(self.numSentences)
        info += "\n Number of total words:\t" + str(self.numWords)
        info += "\n Average Word length: \t" + str(self.avgWordLength)
        info += "\n Average words per sentence:\t" + str(self.avgWordsPerSent)
        info += "\n \nPunctuation:"
        info += "\n Number of question marks:\t" + str(self.questCount)
        info += "\n Number of exclamation marks:\t" + str(self.exclCount)
        info += "\n Number of dashes:\t" + str(self.dashCount)
        info += "\n \nParts of Speech:"
        info += "\n Number of nouns:\t" + str(self.nounCount)
        info += "\n Percentage of nouns:\t" + str(self.nounPerc) + "%"
        info += "\n Number of verbs:\t" + str(self.verbCount)
        info += "\n Percentage of verbs:\t" + str(self.verbPerc) + "%"
        info += "\n Number of adjectives and adverbs:\t" + str(self.adCount)
        info += "\n Percentage of adjectives and adverbs:\t" + str(self.adPerc) + "%"
        info += "\n Number of pronouns:\t" + str(self.proCount)
        info += "\n Percentage of pronouns:\t" + str(self.proPerc) + "%"

        return info


def uniqueWords(theBlob, theDict):
    '''If the word isn't in the dict. add it, if it is, add to the count. Used for common words and unique words
    '''

    wordBlob = allWords
    theDict = theDict
    #print(allWords)

	#initialize variables
    uniqueWords = 0
    wrongWordCount = 0
    commonWords = 0
    iCount = 0
    
    #initialize arrays
    words = {}
    wrongWords = {}
    tooCommon = ["a", "an", "the", "and"]
    
    
    #For each word in the list
    for aWord in wordBlob:
    	#Count the number of "I"s
    	if aWord == "i":
    		iCount += 1
    		
    	#Find misspelled and made-up words
    	if aWord not in theDict:
    		#Increase the total count of misspelled words
    		wrongWordCount += 1
    		if aWord in wrongWords:
    		#If in the list already, increase the count
    			wrongWords[aWord] = wrongWords[aWord] + 1
    		else:
    			#If not, add the word with a count of 1
    			wrongWords[aWord] = 1
    
        #Add words to the word dictionary
        if len(aWord) > 2 and aWord not in tooCommon:
            #If the word is in the list already
            if aWord in words:
                #Increase the count
                words[aWord] = words[aWord] + 1
            else:
                #If not, add the word with a count of 1
                words[aWord] = 1
                
    #Count unique words (length of word list without the counts)
    uniqueWords = len(words)
    
    #Find common words
    newWords = sorted(words, key=words.get, reverse=True)[:10]
    commonWords = newWords

	
    print("\nWord Lists:\n Number of 'I' uses: " + str(iCount) 
    	+ "\n Number of unique words:\t" + str(uniqueWords) 
    	+ "\n Number of misspelled words:\t" + str(wrongWordCount) 
    	+ "\n\n Top ten common words:\t")
    for comWord in commonWords:
    	#Print top ten common words
		print(str(words[comWord]) + "\t" + comWord)
    
    
    #print all misspelled words
    print("\n Words not in dictionary:")
    for theWord in wrongWords:
    	print(theWord + "(" + str(wrongWords[theWord]) + ")")
    

def analyzeText(fileName):
    '''Create Object and run analysis'''
    print(fileName)
    #Open file and read lines
    textFile = open(fileName, "r")
    textLines = textFile.readlines()

    #Convert the list of lines into a single string
    textString = str(textLines[0])
    textString = textString.lower()

    #Turn the string into a textBlob
    fileBlob = TextBlob(textString)

    #Create LiteraryAnalyzer object
    checkTextBlob = LiteraryAnalyzer(fileBlob)

    #Use object to analyze text
    checkTextBlob.fixWords()
    checkTextBlob.analyzeBlob()
    
    #Print results
    print(checkTextBlob.getInfo())

    '''Use dictionary to compare words and find common, mispelled, and unique'''
    #load dictionary
    dictionary = set(open('Dictionary.txt').read().split())

    #Run function
    uniqueWords(fileBlob, dictionary)

def main():

    analyzeText("Texts/HelenOLoy_Robot.txt");

main()


