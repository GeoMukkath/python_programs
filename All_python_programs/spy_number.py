#Q. Check whether the given number is a spy number or not. 

num = int(input("Enter a num: "));

sum= 0;
prod = 1;
while num != 0: 
	d = num % 10;
	sum = sum + d; 
	prod = prod *d;
	num = num // 10; 
	
if prod == sum:
	print("The given number is a spy number.");
else:
	print("The given number is not a spy number.");
	
	  

