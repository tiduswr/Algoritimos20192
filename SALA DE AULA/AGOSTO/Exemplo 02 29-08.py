qt = int(input('Quantos valores da sequência de Fibornacci você deseja? '))
ant = 1
atu = 1
print('1 1', end = ' ')
cont = 2
while cont < qt:
	prox = ant + atu
	ant = atu
	atu = prox
	print(prox, end = ' ')
	cont = cont + 1