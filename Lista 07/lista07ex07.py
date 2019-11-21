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

def is_multiplo(matriz, valproc):
    quant_mult = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] % valproc == 0:
                quant_mult = quant_mult + 1
    return quant_mult

#------------------------------------------------------------------------------------
matriz = []

cabecalho('Criação de Matriz', 50)
print('\n**Use somente valores inteiros!!\n')
linha = int(input('Insira a Quantidade de Linhas: '))
coluna = int(input('Insira a Quantidade de Linhas: '))
cria_mat(matriz, linha, coluna)

cabecalho('Insira os valores da Matriz', 50)
sol_val_mat(matriz, int)

sair = False

cabecalho('Pesquisa', 50)
while sair is False:
    print()
    valorproc = int(input('Qual o valor que deseja testar? '))
    print()

    print('*Resultado da Pesquisa:\n\nForam encontrados {} Multiplos desse numero'.format(is_multiplo(matriz, valorproc)))
    print('='*50)
    cond = input('Deseja continuar? "S" para Sim e "N" para Não: ').upper()
    while cond != 'S' and cond != 'N':
        cond = input('Por favor utilize apenas "S" para Sim e "N"\npara Não: ').upper()
    if cond == 'S':
        print('='*50)
    if cond == 'N':
        sair = True
cabecalho('Programa Encerrado', 50)