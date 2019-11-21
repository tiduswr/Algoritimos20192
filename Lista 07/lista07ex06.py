def criaVet(vet, tamanho):
    for i in range(tamanho):
        vet.append(0)
    return vet

def solic_val(vetor):
    for i in range(len(vetor)):
        vetor[i] = input('Valor {}: '.format(i+1))
    return vetor

def cabecalho(texto, largura):
    txt = str(texto)
    print('=' * largura)
    print('{:^{}}'.format(txt, largura))
    print('=' * largura)
    return

def concatena_vet(vetor1, vetor2):
    LenNewMat = len(vetor1) + len(vetor2)
    ConcMat = []
    aux = 0
    for i in range(LenNewMat):
        ConcMat.append(0)
    for i in range(len(vetor1)):
        ConcMat[i] = vetor1[i]
    for i in range(len(vetor1),LenNewMat):
        ConcMat[i] = vetor2[aux]
        aux = aux + 1
    return ConcMat
#-------------------------------------------------------------------------------------------
vetor1 = []
vetor2 = []

cabecalho('Criação de Lista 01', 50) 
criaVet(vetor1, int(input('Qual o Tamanho do Vetor? ')))
print('\n*Solicitação de valores da Lista 01: \n')
solic_val(vetor1)
print()

cabecalho('Criação de Lista 02', 50)
criaVet(vetor2, int(input('Qual o Tamanho do Vetor? ')))
print('\n*Solicitação de valores da Lista 01: \n')
solic_val(vetor2)
print()

cabecalho('Lista Resultante', 50)
vetorCon = concatena_vet(vetor1, vetor2)
print('Listas concatenadas:',vetorCon)