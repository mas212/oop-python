class A:
	"""docstring for ClassName"""
	def show(self):
		print("ini class A")

class B:
	"""docstring for ClassName"""
	def show(self):
		print("ini class B")

class C(A, B):
	def show(self):
		print("hallo C")

object = C()
object.show()
		
		