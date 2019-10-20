print('='*50)
print('{:^50}'.format("Questão 03 Lista V"))
print('='*50)
listA = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
PlistA = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
contP = 0
for i in range(0, 10):
	listA[i] = int(input('Insira um Valor Inteiro: '))
	if listA[i] % 2 == 0:
		PlistA[i] = listA[i]
		contP = contP + 1
print('\nNumeros Pares Digitados:\n')
for j in range(0, 10):
	if PlistA[j] != ' ':
		print(PlistA[j], end = ' ')
print('\n\nQuantidade de Numeros Pares Digitados:',contP, '\n')