#Q. Program to check whether the given string is a pallindrome or not. 

string = input("Enter the word : "); 

palli = string[: : -1]; 

if(string == palli):
	print("The given word is a pallindrome."); 
else: 
	print("The given word is not a pallindrome.");