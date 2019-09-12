print('Saiba a média e a soma de 10 numeros digitados:\n')
soma = 0
for i in range(1,11,1):
	num = float(input('Digite um numero: '))
	soma = soma + num
	media = soma / 10
print('\nA soma total dos numeros é: {}\nA média dos numeros digitados é: {}'.format(soma,media))