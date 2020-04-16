#Q. Check whether the given year is a leap year or not. 

year = int(input("Enter the year: ")); 

if (year % 4 ==0 and year% 100 != 0 or year % 400 == 0):
	print("The given year is a leap year. ");
else:
	print("The given year is not a leap year.")