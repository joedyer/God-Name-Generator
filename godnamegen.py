import random
import math

vowels = ['a','e','i','o','u','oo','ur','y']

consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','sh','ch','th']


for i in range(0,50):
	syllables = random.randint(1,6)
	name = ""
	
	if random.random() < .33:
		name = random.choice(consonants)+"'"
	
	for j in range (0, syllables):
		
		ending = random.random()
		
		if ending > .5:
			name = name+random.choice(consonants)+random.choice(vowels)
		else:
			name = name+random.choice(consonants)+random.choice(vowels)+random.choice(consonants)
			if random.random > .33 and j != syllables-1:
				name = name+"-"
	print name
	#comment to test