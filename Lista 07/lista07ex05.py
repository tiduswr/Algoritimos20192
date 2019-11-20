def cria_mat(matriz, linha, coluna):
    for i in range(linha):
        matriz.append([0] * coluna)  
    return matriz

def sol_val_mat(matriz, func):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = func(input('Valor|L{}|C{}:'.format(i+1, j+1)))
    return matriz

def cabecalho(texto, largura):
    txt = str(texto)
    print('=' * largura)
    print('{:^{}}'.format(txt, largura))
    print('=' * largura)
    return

def troca_lin_col_quad(matriz, matriz2, linha, coluna):
    auxm = []
    auxm2 = []
    for i in range(len(matriz)):
        auxm.append([0] * (len(matriz) + 1))
        auxm2.append([0] * (len(matriz) + 1))
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            auxm[i][j] = matriz[i][j]
            auxm2[i][j] = matriz2[i][j]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if (i+1) == linha:
                matriz[i][j] = auxm2[i][j]
                matriz2[i][j] = auxm[i][j]
            if (j+1) == coluna:
                matriz[i][j] = auxm2[i][j]
                matriz2[i][j] = auxm[i][j]
    return

def print_mat(matriz):
    mai_cha = 5
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if len(str(matriz[i][j])) > mai_cha:
                mai_cha = len(str(matriz[i][j]))
    mai_cha_lin = 0
    if len(matriz) > 9 and len(matriz) < 100:
        mai_cha_lin = 6
    elif len(matriz) > 99 and len(matriz) < 1000:
        mai_cha_lin = 7
    else:
        mai_cha_lin = 5
    print('|','{:^{}}'.format('#####', mai_cha_lin), end = ' ')
    for i in range(len(matriz[1])):
        print('|','{:^{}}'.format('Col_{}'.format(i+1), mai_cha), end = ' ')
        if (i+1) == len(matriz[1]):
            print('|')
    for i in range(len(matriz)):
        print('|','{:^{}}'.format('Lin_{}'.format(i+1), mai_cha_lin), end = ' ')
        for j in range(len(matriz[i])):
            print('|','{:^{}}'.format(matriz[i][j],mai_cha), end = ' ')
            if (j+1) == len(matriz[1]):
                print('|', end = ' ')
        print()
#----------------------------------------------------------------------------------------
import time
matriz = []
matriz2 = []

cabecalho('Trocar valor de duas Matrizes de ordem igual', 50)
print('ATENÇÃO!! Esse Programa só organiza as matrizes\ncom até 999 registros!!\n')
ordem = int(input('Digite a ordem para as Matrizes Quadradas: '))
print()
print('*Qual o tipo de dado que você irár registrar?')
print('1) Inteiros\n2) Decimal\n3) Texto\n')
dados = int(input('Digite o numero correspondente a opção: '))
while dados != 1 and dados != 2 and dados != 3:
    dados = int(input('Digite o numero correspondente a opção: '))

if dados == 1:
    dados = int
elif dados == 2:
    dados = float
else:
    dados = str

cabecalho('Solicitação de Valores Matriz 01', 50)
cria_mat(matriz, ordem, ordem)
cria_mat(matriz2, ordem, ordem)
sol_val_mat(matriz, dados)
print()

cabecalho('Solicitação de Valores Matriz 02', 50)
sol_val_mat(matriz2, dados)
print()

cabecalho('Matriz 01', 50)
print()
print_mat(matriz)
print()
time.sleep(2)
cabecalho('Matriz 02', 50)
print()
print_mat(matriz2)

cabecalho('Insira a Linha e Coluna para trocar', 50)
lin_mud = int(input('Insira a linha Trocar: '))
col_mud = int(input('Insira a coluna para Trocar: '))
print()

troca_lin_col_quad(matriz, matriz2, lin_mud, col_mud)
print()

cabecalho('Resultado das trocas', 50)
print('\nMatriz 01')
print_mat(matriz)
print('\nMatriz 02')
print_mat(matriz2)