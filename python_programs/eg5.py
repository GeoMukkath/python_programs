num = int(input("Enter the number : "));
sum =0 ;
for x in range(num):
	if (x%3 == 0 or x%5 == 0) :
		sum = x + sum;

print(sum);
	   
