#Deixando o programa amigavel:
print('=' * 50)
print('{:^50}'.format('Banco 24hrs'))
print('='*50)
valor = int(input('Quanto você deseja sacar? R$ '))
print('')
#Nomeando variaveis:
total = valor
ced = 100
totced = 0
#Tive que aprender esse código novo, pois eu não estava conseguindo fazer de outra forma que foi explicada na aula:
while True:
#Ele vai passar por esse If se o Valor Total for maior ou igual ao da cédula e adicionar mais 1 ao contador na cedula:
	if total >= ced:
		total = total - ced
		totced = totced + 1
#Quando ele esgotar as possibilidades com uma das cedulas ele vai printar quantas cedulas ele conseguiu tirar do total e qual era o valor da cedula:
	else:
		if totced > 0:
			print('Você recebera {} cédula(as) de R$ {}'.format(totced,ced))
#Depois ele vai trocar os valores da cedula até conseguir zerar o valor total informado no inicio do programa:
		if ced == 100:
			ced = 50
		elif ced == 50:
			ced = 20
		elif ced == 20:
			ced = 10
		elif ced == 10:
			ced = 5
		elif ced == 5:
			ced = 1
#É muito importante zerar as cedulas no final, pois se não o programa vai misturar a quantidade de todas as cedulas:
		totced = 0
#Quando ele conseguir zerar o valor total ele vai parar o looping:
		if total == 0:
			break
#Abaixo é somente uma linha para deixar o programa mais amigavel:
print('\nObrigado por usar nosso Banco 24hrs!\n')
print('=' * 50)
print('{:^50}'.format('Volte Sempre!'))
print('='*50)