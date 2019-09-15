somaright=somaleft=0
qtd = int(input('\nDigite quantos termos você quer: '))
print('')
for i in range(1,qtd+1):
    ant = i - 1
    atual = i + ant
    print('{}/{}'.format(i,atual))
    somaright = somaright + atual
    somaleft = somaleft + i
print('')
print('Soma: {} / {}'.format(somaleft,somaright))