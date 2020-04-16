#Q. Write a program to check whether the given program is an armstrong number or not. 

num = int(input("Enter a number: "));
og = num;
sum =0 ;
dig =0;
cube = 0;
while num != 0:
	dig = num % 10;
	cube = dig ** 3;
	sum = sum + cube ; 
	num = num // 10;
	
if og == sum :
	print("The given number is an armstrong number. ");
else:
	print("The given number is not an armstrong number.");
		