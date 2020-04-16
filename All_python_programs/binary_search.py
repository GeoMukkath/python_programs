#Binary search
lst = [12,33,34,56,62,77,79,34];
num= int(input("Enter the number you want to search in the list: ")); 
i = 0;
j = len(lst) - 1;
found = False; 
while i<=j and found == False:
	m= (i +j) // 2;
	if lst[m] == num:
		print("The number exists");
		found = True; 
	elif num < lst[m]:
		j = m -1 ; 
	else:
		i = m +1; 

if found == False:
	print("The number does not exist in the list");					