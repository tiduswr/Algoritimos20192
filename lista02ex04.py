print('Organizar do maior para o menor: ')
men = float(input('Digite o primeiro numero: '))
med = float(input('Digite o segundo numero: '))
mai = float(input('Digite o terceiro numero: '))
if men >= med or med >= mai:
	if men > med:
		aux = men
		men = med
		med = aux
	if med > mai:
		aux = med
		med = mai
		mai = aux
	if men > med:
		aux = men
		men = med
		med = aux
print('A sequência correta dos numeros é: \n {} - {} - {}'.format(men, med, mai))