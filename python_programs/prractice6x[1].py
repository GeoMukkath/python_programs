class A:
	
	def __init__(self):
		print("In init A");
		
	def feat1(self):
		print("Feature 1 is working ")
	
	def feat2(self):
		print("Feature 2 is working ")

class B():
	
	def __init__(self):
		super().__init__();
		print("In B init");
	
	def feat3(self):
		print("Feature 3 is working")
		
	def feat4(self):
		print("Feature 4 is working")

class C(A,B):
	
	def __init__(self):
		super().__init__();
		super().feat4();
		print("In init C");

c  = C();