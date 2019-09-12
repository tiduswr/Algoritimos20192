print('SAIBA QUAL O MAIOR E O MENOR VALOR')
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
print('O maior numero é {:.0f} e o menor é {:.0f}'.format(mai, men))