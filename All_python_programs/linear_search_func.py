def linear_search(lst,num):
	found = False ;
	i = 0;
	while i < len(lst) and found == False:
		if lst[i] == num:
			found = True;
		else:
			i = i + 1 ; 		
	return found;			
lst = [90,456,89,234,67,99,24,78];
num = int(input("Enter the value: "));
print(linear_search(lst,num));
