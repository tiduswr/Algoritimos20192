print('Saiba qual o maior numero dentre os digitados: ')
num = float(input('Digite um numero: '))
men = num
mai = num
for repet in range(1,11,1):
	num = float(input('Digite outro numero: '))
	if num > mai:
		mai = num
	if num < men:
		men = num
print('O maior numero digitado é {} e o menor é {}.'.format(mai,men))