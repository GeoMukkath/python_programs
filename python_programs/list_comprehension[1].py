import random
#print numbers from 1 to 9 
io = [x for x in range(10)]
print(io)

io1 = [y*2 for y in range(11) ]
print(io1)

io2 =[i for i in range(11) if i%2 == 1]
print(io2)

io3 = [k for k in range(101) if k%10 == 0]
print(io3)

sen = "I love 2 t0 go to the 5tore 3 t1mes a week"
io4 = [c for c in sen if c.isnumeric()]
print(io4)

names = ["john", "kalki", "Favian", "jonathan"]
io5 = [d for d,e in enumerate(names) if d == "Favian"]
print(io)

