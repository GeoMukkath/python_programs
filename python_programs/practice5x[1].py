class A:
	def feat1(self):
		print("Feature 1 is working ")
	
	def feat2(self):
		print("Feature 2 is working ")

class B(A):
	def feat3(self):
		print("Feature 3 is working")
		
	def feat4(self):
		print("Feature 4 is working")

class C(B):
	def feat5(self):
		print("Feature 5 is working")		

a1 = A();

a1.feat1();
a1.feat2();

b1 = B();

b1.feat1();
b1.feat2();
b1.feat3();
b1.feat4();

c1= C();

b1.feat1();
b1.feat2();
b1.feat3();
b1.feat4();
c1.feat5();

