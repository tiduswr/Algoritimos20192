def criaVet(vet, tamanho):
    for i in range(tamanho):
        vet.append(0)
    return vet

def solic_val(vet, tamanho):
    for i in range(tamanho):
        vet[i] = input('Valor {}: '.format(i+1)).upper()
    return vet

def invert_vet(vet,tamanho):
    aux = []
    for i in range(tamanho):
        aux.append(0)
        aux[i] = vet[i]
    for i in range(tamanho):
        vet[tamanho - (i+1)] = aux[i]
    return vet

def cabecalho(texto):
    txt = str(texto)
    print('=' * 50)
    print('{:^50}'.format(txt))
    print('=' * 50)
    return
#---------------------------------------------------------------------------
vetor = []

cabecalho('Inverta a Ordem de um Vetor')
tamanho = int(input('Qual o tamanho do vetor? '))
print()

vetor = criaVet(vetor, tamanho)

cabecalho('Insira os valores para reverter')
vetor = solic_val(vetor, tamanho)
print()

cabecalho('Resultado')
print(invert_vet(vetor, tamanho))