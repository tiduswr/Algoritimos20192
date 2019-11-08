#Definição de Variaveis:
matriz = []
aux = 0

#Criando Matriz:
for i in range(4):
    matriz.append([0] * 4)

#Cabeçalho para o programa:
print('\n','=' * 60)
print('{:^60}'.format('SAIBA OS VALORES MAIORES QUE 10 EM UMA MATRIZ 4X4 !!'))
print('=' * 60)

#Solicitação dos valores da Matriz 4 x 4:
for i in range(4):
    for j in range(4):
        matriz[i][j] = float(input('Matriz: Linha {} | Coluna {}: '.format(i+1, j+1)))
        if matriz[i][j] > 10:
            aux = aux + 1

#Condições para Impressão de Informação:
if aux == 0:
    print('\n','Todos os valores digitados são menores que 10!\n\nPrograma encerrado.')
else:
    print('\n','Você digitou', aux,'numeros maiores que 10!\n\nPrograma encerrado.')