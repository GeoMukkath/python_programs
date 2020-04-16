# exercise 33 of practicepython.org 
print("Welcome to the birthday dictionary. We know the birthdays of :  ");

print(" 1. Geo Mukkath\n 2. Roger Fedrer \n 3. Ralph Lauren\n 4. Mark Cuban");

a = ["Geo Mukkath", "08/10/1996"];
b = ["Roger Fedrer", "11/07/1982"];
c = ["Ralph Lauren", "27/12/1965"];
d = ["Mark Cuban", "17/02/1979"]; 
 
name = input("Who's birthday do you want to look up ?\n");
if name == a[0]:
 	print("%s's birthday is on %s" %(a[0],a[1]));
elif name  == b[0]:
 	print("%s's birthday is on %s" %(b[0],b[1]));
elif name == c[0]: 
	print("%s's birthday is on %s" %(c[0],c[1])); 	
elif name == d[0]:
	print("%s's birthday is on %s" %(d[0],d[1]));
 	
 