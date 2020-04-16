#program for fahrenheit - cel and cel - fahrenheit conversion . 

def fa_cel( ):
	f = float(input("Input fahrenheit value: "));
	c= (f-32) * 5/9 ;
	print(c);
	 		
def cel_fa( ):
	c = float(input("Input the celcius value: "));
	f = (c/5)*9 + 32; 
	print(f);
	
n = int(input("For fahrenheit to celcius press 1 | For celcius to fahrenehit press 2 : "));

f = 0 ; 
c = 0 ; 

if n ==1 :
 	fa_cel( );
else:
 	cel_fa( );
 