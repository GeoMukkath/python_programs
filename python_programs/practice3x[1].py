class human:
	
	no_of_hands  = 2 
	
	def __init__(self):
		self.name = "Geo"
		self.age = 23
		self.job = "engineer"
		self.height = "5'7"

c1 = human();
c2 = human();

print(c1.name, c1.age, c1.job, c1.height, human.no_of_hands);

c2.name = "Bebo"
c2.job = "analyst"

print(c2.job);	
		
