print('Maior e menor entre 15 numeros')
valor = float(input('Digite um valor: '))
menor = valor
maior = valor
for i in range(14):
	valor = float(input('Digite outro valor: '))
	if valor < menor:
		menor = valor
	if valor > maior:
		maior = valor
print('Menor', menor)
print('Maior', maior)