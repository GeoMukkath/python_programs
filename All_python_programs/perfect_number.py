#Q. Check whether the given number is a perfect number or not. 

num = int(input("Input a number: ")); 
sum = 0 ;
for i in range(1,num):
	if num % i == 0 :
		sum = sum + i ;

if sum == num:
	print("The given number is a perfect number. ");
else:
	print("The given number is not a perfect number.")