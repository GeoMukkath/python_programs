# program to check whether a given number is a strong number or not. 

num = int(input("Enter a number: ")); 
fact = 0; 
while num != 0:
	dig = num%10;
	for i in range(1,dig):
		fact = fact * i;
		print(fact); 
