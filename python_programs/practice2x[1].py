class profile:
	
	def __init__(self):
		self.name = "Geo";
		self.age = 23;
	
	def update(self):
		self.age = 23; 	
	
	def compare(self,candidate2):
		if self.age == candidate2.age:
			return True;
		else:
			return False;
				
candidate1 = profile();
candidate2 = profile();
candidate2.update();
candidate2.name = "Rohit";

if candidate1.compare(candidate2):
	print("The age is the same.")
else:
	print("The ages are different.")
	
