#Q. Swap two numbers. 

x = int(input("Enter the value of X: "));
y = int(input("Enter the value of Y: ")); 
temp = 0 ; 
print("BEFORE SWAP : \n X = %d  Y = %d" %(x,y));

temp =x ;
x = y;
y = temp ;

print("AFTER SWAP: \n X= %d Y = %d" %(x,y));

    