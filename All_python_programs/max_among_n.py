#Q. Find the maximum among n numbers given as input. 

n = int(input("Enter the number of numbers : ")); 
print("Enter the numbers: "); 
a = [ ];
for i in range(n):
	num = int(input( ));
	a.append(num); 

maximum= max(a);
print("The maximum among the given list is %d" %maximum); 