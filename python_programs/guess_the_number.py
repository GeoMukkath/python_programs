#### RANDOM GUESS GAME BY GEO MUKKATH #####

import random ; 

num = random.randrange(101);
nofguess = 1 ; 
guess = 0 ;
while guess != num:
	guess = int(input("Guess the number between 1 and 100: "));
	if num > guess:
		print("Your guess is less than the number. ");
		nofguess = nofguess + 1;
	elif num < guess:
		print("Your guess is greater than the number.");
		nofguess = nofguess+ 1;
	else:
		print("You have guessed correctly in %d guesses" %nofguess);
		