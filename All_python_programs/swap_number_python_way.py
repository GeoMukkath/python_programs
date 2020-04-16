#Q. Swap number using third variable 

x = int(input("Enter the value of X: " )); 
y = int(input("Enter the value of  Y: "));

print("BEFORE SWAP: \n X= %d  Y = %d" %(x,y));

x,y = y,x ; 

print("AFTER SWAP: \n X= %d Y = %d" %(x,y));