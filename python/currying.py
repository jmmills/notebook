import timeit
def a(test):
	yar = 'soup'

	def b():
		print(yar)
		print(test)
	
	print(timeit.timeit(b, number=100))

a('testing')

