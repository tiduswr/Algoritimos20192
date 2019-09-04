num = int(input('DIVISORES DE UM NUMERO INTEIRO\nQual o Valor? '))
for i in range(1,num+1,1):
	if num % i == 0:
		print(i,end=' ')
#Forma mais eficiente
num = int(input('\nDIVISORES DE UM NUMERO INTEIRO\nQual o Valor? '))
print('1')
for i in range(2,num,1):
	if num % i == 0:
		print(i,end=' ')
print(num)
