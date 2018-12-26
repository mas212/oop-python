class Product:
	def __init__(self, name, qty, price, description):
		self.name 			= name
		self.qty 			= qty
		self.price 			= price
		self.description 	= description

	def stock(self):
		print("stock masih " + str(self.qty))

	def cart(self, qty, price):
		addToCart  = self.price * self.qty
		return addToCart 

	def discount(self, price):
		pricePublish = self.price 
		if(pricePublish > 1000):
			print('anda dapat discount')
		else:
			print('belum dapet discount')

Items = Product("rokok", 10, 10000, "yes ada")

Items.stock()
# print(Items.cart(10000,2))

Items.discount(100)