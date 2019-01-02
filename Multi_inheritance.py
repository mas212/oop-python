class A :
	def method_A(self):
		print("method A")

class B:
	def method_B(self):
		print("method B")

class  C(A, B):
	pass

object = C();
object.method_A()
object.method_B()
		
		