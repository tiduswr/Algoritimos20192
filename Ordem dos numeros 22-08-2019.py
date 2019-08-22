print('Digite três valores em ordem crescente.')
menor = int(input('Menor valor: '))
meio = int(input('Valor intermediario: '))
maior = int(input('Maior Valor: '))
if menor >= meio or meio >= maior:
	print('Ta querendo me trolar? Esta errado!!! ')
	if menor > meio:
		aux = menor
		menor = meio
		meio = aux
	if meio > maior:
		aux = meio
		meio = maior
		maior = aux
	if menor > meio:
		aux = menor
		menor = meio
		meio = aux
print('Essa é a ordem correta: ', menor, meio, maior)