def lvetor(vetor,tam):
	for i in range(tam):
		vetor[i] = int(input('Valor da posição {}: '.format(i+1)))

def imprimir(vetor,tam):
	for i in range(tam):
		print(vetor[i], end = ' ')
	print()

def encontrar(vetor,tam,valor):
	for i in range(tam):
		if valor == vetor[i]:
			return True
	return False

n = int(input('Tamanho do Vetor: '))
v = [0] * n

lvetor(v, n)

imprimir(v, n)

valor = int(input('Que Valor deseja Procurar? '))

if encontrar(v, n, valor):
	print('Encontrado! ')
else:
	print('Não Encontrado')
