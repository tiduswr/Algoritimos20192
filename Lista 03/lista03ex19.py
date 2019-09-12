print('='*50)
print('{:.^50}'.format('Lojinha de R$ 1.00'))
print('='*50)
num = int(input('Digite quantos produtos o cliente esta\nlevando: '))
calc = 0
for i in range(1,num+1,1):
	calc = (calc - 0.01) + 2
	print('{} - R$ {:.2f}'.format(i,calc))
print('='*50)
print('{:.^50}'.format('Obrigado!'))
print('='*50)