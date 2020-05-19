import threading 
import time
import enchant 
import random
from collections import Counter

score = 0
def genLetterPool(): 
	vowels = ['a', 'e', 'i', 'o', 'u']
	letters = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p','r', 's', 't', 'v', 'w', 'x', 'y']

	s = '' 

	for n in range(2):
		s+=random.choice(vowels) 

	for n in range(4):
		s+=random.choice(letters)

	return s

def isWord(str):
	d = enchant.Dict('en_US')
	return d.check(str)

def isFrom(guess, ana):

	for n in range(len(guess)): 
		if guess[n] not in ana: 
			return False

	guessCt = Counter(guess)
	anaCt = Counter(ana)

	anaCt.subtract(guessCt)

	for n in range(len(guess)):
		if anaCt[guess[n]] < 0:
			return False
	return True 


def play():
	global score
	ana = genLetterPool()
	anaList = list(ana)
	printedList = "  ".join(anaList)
	guesses = []
	print('Welcome to Anagrams: You have 60 seconds to try to make words out of the letters in the bank (2-6 Letter words only)')
	while True: 
		print("Bank: ",printedList) 
		guess = input("Guess (Min. 2 Letters): ").strip()

		if len(guess) < 2 or len(guess) > 6: 
			print("Sorry, guesses must be between 2 and 6 letters\n")
			continue
		if isWord(guess) == False: 
			print("Sorry, this is not a real word\n")
			continue
		if isFrom(guess, ana) == False: 
			print("This guess is not valid given the bank\n")
			continue
		if guess in guesses: 
			print("Sorry, you've already guessed this!\n")
			continue

		guesses.append(guess) 
		leng = len(guess) 
		if(leng == 2):
			score += 100
			print("Good job! Current Score: ",score,'\n')
		if(leng == 3):
			score += 200
			print("Great job! Current Score: ",score,'\n')
		if(leng == 4):
			score += 400
			print("Wow! Current Score: ",score,'\n')
		if(leng == 5):
			score += 1000
			print("Sweet! Current Score: ",score,'\n')
		if(leng == 6):
			score += 2000
			print("Perfect! Current Score: ",score,'\n')

t = threading.Thread(target = play)
t.daemon = True
t.start() 

time.sleep(60)
print("Out of time! Final Score: ",score)
