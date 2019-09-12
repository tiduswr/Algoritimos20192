#Imprima os N primeiros numeros primos onde N é informado pelo Usuario!
quant = int(input('Quantos Primos? '))
print(1)
numero = 2
cont = 1
while cont < quant:
	primo = True
	for i in range(2,numero,1):
		if numero % i ==0:
			primo = False
	if primo:
		print(numero)
		cont = cont + 1
	numero = numero + 1
			