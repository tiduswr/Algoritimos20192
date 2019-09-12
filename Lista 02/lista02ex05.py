print('PRODUTO MAIS BARATO')
p1 = float(input('Digite o valor do Primeiro Produto: '))
p2 = float(input('Digite o valor do Segundo Produto: '))
p3 = float(input('Digite o valor do Terceiro Produto: '))
if p1 == p2 and p1 and p2 < p3:
	print('Os Produtos 1 e 2 são os mais baratos!')
elif p2 == p3 and p2 and p3 < p1:
	print('Os Produtos 2 e 3 são os mais baratos!')
elif p3 == p1 and p3 and p1 < p2:
	print('Os Produtos 1 e 3 são os mais baratos!')
elif p1 < p2 and p3:
    print('O Produto mais barato é o Primeiro! ')
elif p2 < p3 and p1:
	print('O produto mais barato é o Segundo! ')
elif p3 < p2 and p1:
	print('O Produto mais barato é o Terceiro! ')
else:
	print('Todos os valores são iguais! ')