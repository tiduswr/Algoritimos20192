print('Maior e menor entre 15 numeros')
qt = int(input('Digite quantos numeros você deseja testar: '))
valor = float(input('Digite um valor: '))
menor = valor
maior = valor
soma = valor
for i in range(qt-1):
	valor = float(input('Digite outro valor: '))
	soma = soma + valor
	if valor < menor:
		menor = valor
	if valor > maior:
		maior = valor
print('')
print('Menor', menor)
print('Maior', maior)
print('Soma', soma)