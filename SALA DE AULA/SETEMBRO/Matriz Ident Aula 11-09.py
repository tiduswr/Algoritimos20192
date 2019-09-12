#Solicitar ao usuario uma dimensão e imprimir a matriz identidade correspondente
dimensao = int(input('Por favor, digite a dimensão: '))
for linha in range(dimensao):
	for coluna in range(dimensao):
		if linha == coluna:
			print(1, end = ' ')
		else:
			print(0, end = ' ')
	print()