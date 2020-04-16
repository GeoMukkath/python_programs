#Operators in python 

int1 = 5;
int2 = 10;
int3 = 23;

#addition
sum = int1 + int2 ;
print(sum); 

#sustraction 
diff = (int1 - int2) ;
print(diff); 

#multiplication
prod = int1 * int2 ;
print(prod);

#division 
div = (int2/int1) ;
print(div);

#Modulus 
rem = int3%int2;
print(rem);

# Using two multiplication operators results in power relationship 

squared =  7 ** 2; #This equates to 7 raised to 2  
print(squared); 

cubed = 2 **3; # This equates to 2 raised to 3 
print(cubed); 

#concatenation 
#string concatenation using addition operator 
name1 = "Geo"; 
name2 = "Mukkath"

print(name1+" "+name2);

print("Word1"+ " "+"Word2" );

# If you multiply a string with an integer then it displays the string that many times 
lotsofhellos = "hello " * 10 ;  
print(lotsofhellos); 

#using operators with lists 
odd_list  = [1,3,5,7 ];
even_list = [2,4,6,8];

alllist = odd_list+even_list ; 
print(alllist); 
