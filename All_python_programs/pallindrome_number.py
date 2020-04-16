#Q. Program to find whether the given number is a pallindrom or not .  

num = int(input("Enter the given number: ")); 
og = num;
palli = 0 ;
#palli = num % 10 ; 
#print(palli); 
while num !=0:
	dig = num % 10;
	palli = palli *10 + dig; 
	num = num // 10;
	
if og == palli:
	print("The given number is a pallindrome.");
else:
	print("The given number is not a pallindrome.");
	
	