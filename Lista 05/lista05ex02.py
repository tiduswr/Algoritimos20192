print('='*50)
print('{:^50}'.format("Questão 02 Lista V"))
print('='*50)
listA = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
QlistA = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
for i in range(0, 10):
	listA[i] = int(input('Insira um Numero Real: '))
	QlistA[i] = listA[i] **2
print('\nConjunto dos numeros digitados: \n',listA)
print('\nConjunto dos Quadrados dos numeros digitados:\n', QlistA)