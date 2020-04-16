#progwithmosh

def fizz_buzz() : 
	num = int(input("Enter the number : "));
	if((num%3==0) & (num%5==0)):
		print("fizzbuzz");
	elif num % 3== 0:
		print("fizz");
	elif num % 5== 0:
		print("buzz");
	else:
		print(num);  
	
fizz_buzz( );