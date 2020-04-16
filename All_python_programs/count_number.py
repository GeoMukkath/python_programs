#Q. Program to count the number of digits in a number. 

a = int(input("Enter the number: ")); 
count = 0 ;
while a != 0:
	d = a % 10;
	count = count +1;
	a = a // 10 ; 

print(count);
