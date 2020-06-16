#string
a= 'string';
print(a[2],a[5]);

#list
b= [23,'numeral','fortran',88,'tagline'];
print(b[3]);
print(b[2]);

#tuple
c = ('Joy', 'Stan', 'edge', 'vase');
print(c[1]);
print(c[3]);

#slicing 
prose = "internet"
print(prose[1:7])
print(prose[1:])
print(prose[:8])
print(prose[-1])
print(prose[-3:])
print(prose[:-3])

#concatenation

x= "diu" + "daman"
print(x)

y=['yamaha','jawa','hummer'] + ['bajaj', 'hero']

print(y)

z= ('java', 'python' ,'pontiac') + ('subaru',)
print(z)

# in statement

x = "owl"
print("w" in x)

y = ['pi', 'lambda', 'theta', 'kappa']
print('theta' not in y )
print('kappa' in y)

z = ('sprite', 'coca-cola', 'intex', 'book')
print('intex' in z)

# min 

z = ('sprite', 'coca-cola', 'intex', 'book')
print(min(z))

g = [23,34,12,45,0.67]
print(min(g))

k = "unicorn"
print(min(k))

# sorted - returns only as a list

oil = ('shell', 'aramco', 'texasoil')
print(sorted(oil))

electronics = ['sony', 'logitec', 'lenovo']
print(sorted(electronics))

watch = "citizen"
print(sorted(watch))

mobile = ['xiaomi', 'oppo', 'xiaomi', 'nokia', 'samsung']
print(mobile.count('xiaomi'))

car = 'tata'
print(car.count('a'))

#list

vehicle = ('car', 'plane', 77, 'cipherpol01', '0.87', '9.88')

v = list(vehicle)
print(v)

#append

num1 = [23,88,45,32,92,4,12]
num1.append(44)

print(num1)

num2 = [45,33,90,7,82]
num1.extend(num2)
print(num1)

num1.pop(1)
print(num1)

num2.reverse()
print(num2)

num2.insert(2,66)
print(num2)

num1.sort()
print(num1)
num1.sort(reverse= True)
print(num1)

# tuple

integers = [23,33,2,90,87,65,52]

uni = tuple(integers)
print(uni)

