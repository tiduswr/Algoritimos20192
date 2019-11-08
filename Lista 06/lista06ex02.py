#Nomeando Variaveis:
matriz = []
o = 5
local = ''
japrint = False
plural = 0
continuar = True
encont = False

#Cabeçalho para o programa:
print('=' * 60)
print('{:^60}'.format('Pesquise um valor na Tabela 5 x 5!!'))
print('=' * 60)

#Criando Matriz:
for i in range(o):
    matriz.append([0] * o)

#Inserindo Valores na Matriz:
for i in range(o):
    for j in range(o):
        matriz[i][j] = input('Matriz - Linha {} | Coluna {}: '.format(i+1, j+1))
print('=' * 60)
print('{:^60}'.format('PESQUISA'))
print('=' * 60)

#Condição de Continução de pesquisa:
while continuar == True:

    #Reset da Variavel para Printar:
    japrint = False

    #Solicitação do Valor para pesquisa:
    X = input('\nQual o valor para pesquisar? ')
    print()

    #Verifica se há mais de uma Variavel, para formatar o texto em Plural ou singular:
    for i in range(o):
        for j in range(o):
            if matriz[i][j] == X:
                plural = plural + 1
    if plural > 1:
        pl1 = 's'
        pl2 = 's'
        pl3 = 'is'
    else:
        pl1 = ''
        pl2 = ''
        pl3 = 'l'
    plural = 0

    #Pesquisa o Numero e Printa o resultado formatado:
    print('=' * 60)
    print('{:^60}'.format('RESULTADO DA PESQUISA'))
    print('=' * 60)
    for i in range(o):
        for j in range(o):
            if matriz[i][j] == X:
                encont = True
                if japrint == False:
                    print('A pesquisa encontrou o{} seguinte{} loca{}:\n'.format(pl1, pl2, pl3))
                    japrint = True
                local = str('Linha '+ str(i+1) + ' Coluna '+ str(j+1))
                print('Pesquisa = "{}" --> Matriz - {}'.format(X, local))

    #Condição caso não seja encontrado um numero:
    if encont == False: 
        print('Nenhum valor encontrado para: Pesquisa = "{}".'.format(X))
    print()
    print('=' * 60)
    print()

    #Verificar se o Usuario deseja continuar a pesquisa:
    reiniciar = input('Deseja Procurar outro Valor(S - SIM | N - NÃO)? ').upper()
    while reiniciar != 'S' and reiniciar != 'N':
        print('\nPor Favor, digite apenas "S" ou "N"!!\n')
        reiniciar = input('Deseja Procurar outro Valor(S - SIM | N - NÃO)? ').upper()
    if reiniciar == 'S':
        continuar = True
    else:
        continuar = False
    
    #Reset de Variavel:
    encont = False

#Rodapé do programa:
print('=' * 60)
print('{:^60}'.format('Programa Encerrado!'))
print('=' * 60)
