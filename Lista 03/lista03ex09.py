print('{:=^50}'.format('Tabuada!'))
num = int(input('Por favor, insira um numero inteiro: '))
print('='*50)
print('')
for i in range(1,11,1):
	soma = num + i
	sub = num - i
	div = num / i
	mult = num * i
	print('{} + {} = {} / {} - {} = {} / {} ÷ {} = {:.2f} /{} x {} = {} '.format(num,i,soma,num,i,sub,num,i,div,num,i,mult))