for x in range(2,9,2):
	for y in range(1,10,2):
		fxy = (x**4 + (3*x)*y + y**3)/((2*x)*y + 3*x + 4*y + 2)
		print('Para X = {} e Y = {} a Função f(X,Y) = ~ {:.2f}.'.format(x, y, fxy))