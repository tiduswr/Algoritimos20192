valor = int(input('Insira um valor para o calculo de Fatorial: '))
fat = 1
for i in range(valor,1,-1):
	fat = fat * i
print(fat)