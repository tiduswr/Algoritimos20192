lin = 5
col = 10
matriz = []
gabarito = [0] * col
acertos = [0] * lin

for i in range(lin):
    matriz.append([0] * col)

print('=' * 56)
print('{:^56}'.format('Insira o Gabarito'))
print('=' * 56)

for i in range(col):
    gabarito[i] = input('Por Favor Insira a Resposta da Questão {}: '.format(i+1)).upper()

print('=' * 56)
print('{:^56}'.format('As respostas dos alunos'))
print('=' * 56)

for i in range(lin):
    print('\n* Aluno 0{}:\n'.format(i+1))
    for j in range(col):
        matriz[i][j] = input('Por Favor Insira a Resposta da Questão {}: '.format(j+1)).upper()

for i in range(lin):
    for j in range(col):
        if matriz[i][j] == gabarito[j]:
            acertos[i] = acertos[i] + 1

print('=' * 56)
print('{:^56}'.format('Resultados'))
print('=' * 56)

for j in range(lin):
    print('|','{:^8}'.format('Aluno_'+str(j+1)), end = ' ')
    if (j + 1) == lin:
        print('|', end = '')
print()

for i in range(lin):
    print('|', '{:^8}'.format(acertos[i]), end = ' ')
    if (i + 1) == lin:
        print('|', end = '')
print()