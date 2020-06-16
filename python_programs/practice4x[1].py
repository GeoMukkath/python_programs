class student:
	
	college ="FCRIT" ;	
	def __init__(self,m1,m2,m3):
		self.m1 = m1 ;
		self.m2 = m2 ; 
		self.m3 = m3 ; 
		self.lap = self.laptop()
		
	def avg(self):
		return (self.m1 + self.m2 + self.m3) / 3				

	@classmethod
	def info(cls):
		return cls.college ; 

	class laptop:
		
		def __init__(self,brand,ram,bit):
			self.brand = "Lenovo"
			self.ram = "8GB" 
			self.bit ==64
			
		def show(self):
			print(self.brand) 

s1 = student(23,44,77);

average_marks = s1.avg();

print(average_marks);

lap = student.laptop();

student.laptop.show();
