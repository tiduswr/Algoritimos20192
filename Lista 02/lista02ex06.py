print('ORGANIZADOR DE NUMEROS EM FORMA DECRESCENTE!')
print('-----------------------------------------------------\n')
n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
n3 = float(input('Digite o terceiro numero: '))
if n1 <= n2 or n2 <= n3 or n1<= n3:
	if n1 < n2:
		aux = n1
		n1 = n2
		n2 = aux
	if n2 < n3:
		aux = n2
		n2 = n3
		n3 = aux
	if n1 < n2:
		aux = n1
		n1 = n2
		n2 = aux
print('\n A sequencia dos numeros em forma decrescente é: {} - {} - {}' .format(n1, n2, n3))