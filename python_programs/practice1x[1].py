class computer:
	def __init__(self,cpu,ram):
				 self.cpu = cpu;
				 self.ram = ram;   
    			
	def config(self):
		print("config is", self.cpu, self.ram );
		
comp1 = computer('i7','8gb');
comp2 = computer('AMD','16gb');

comp1.config();
comp2.config();
		