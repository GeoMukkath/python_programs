#.Q. Check whether the given number is automorphic or not. 

num = int(input("Enter the number: ")); 

sq = num ** 2;
d1 = num % 10;
d2 = sq %10;

if d1 == d2:
	print("The given number is automorphic.");
else : 
	print("The given number is not automorphic."); 
	