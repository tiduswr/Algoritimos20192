print('='*50)
print('{:^50}'.format("Questão 03 Lista V"))
print('='*50)
listA = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
maior=pos=0
for i in range(0,10):
	listA[i] = int(input('Digite um numero inteiro: '))
	if listA[i] > maior:
		maior = listA[i]
		pos = i + 1
print('\nNumeros digitados:\n', listA,'\n')
print('Maior Numero Digitado: ', maior,'\nPosição na Lista: ', pos,'\n')