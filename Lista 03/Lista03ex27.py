qtd = int(input('Quantas vezes você quer calcular "N"? '))
for i in range(1,qtd+1):
    calc = 1 / i
    print('1/{} = {}'.format(i,calc))