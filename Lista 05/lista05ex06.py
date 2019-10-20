print('='*50)
print('{:^50}'.format("Questão 06 Lista V"))
print('='*50)
listA = [' ']*10
InlistA = [' ']*10
for i in range(10):
	x = 9
	listA[i] = input('Insira um Caractere: ')
	x = x - i
	InlistA[x] = listA[i]
print('\nLista Digitada:\n\n{}\n'.format(listA))
print('\nLista Invertida:\n\n{}'.format(InlistA))