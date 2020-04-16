lst = [23,25,67,34,9,42,89,22,19,67] ;

num = int(input("Enter the number you want to search: ")); 
found = False; 
i = 0 ;
while i < len(lst) and found == False:
	if lst[i] == num:
		found = True;
	else:
		i = i + 1 ;

if found == True:
	print("Yes %d exists in the list at position %d" %(num,i));
else:
	print("No %d does not exist in the list" %num);			