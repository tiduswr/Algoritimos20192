print('='*50)
print('{:^50}'.format("Questão 01 Lista V"))
print('='*50)
A = [1, 0, 5, -2, -5, 7]
print(A, '\n')
somA = A[0] + A[1] + A[5]
print('Soma Posição 0, 1 e 5:' , '\n', A[0], '+', A[1], '+', A[5], '=', somA,'\n')
A[4] = 100
for i in range((len(A))):
	print('Valor da Posição',i,':',A[i])