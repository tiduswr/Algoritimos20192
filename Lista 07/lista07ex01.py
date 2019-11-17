#Funções:

def criaVet(vet, tamanho, func):
    for i in range(tamanho):
        vet.append(func(input('Vetor | Item {}: '.format(i+1))))
    return vet

def vet_print_par_or_impar(vet):
    print('Pares:')
    for i in range(len(vet)):
        if vet[i] % 2 == 0:
            print(vet[i],' |', end = ' ')
    print('\nImpares:')
    for i in range(len(vet)):
        if vet[i] % 2 != 0:
            print(vet[i],' |', end = ' ')
    return

def cabecalho(texto):
    txt = str(texto)
    print('=' * 50)
    print('{:^50}'.format(txt))
    print('=' * 50)
    return

# --------------------------------------------------------
#Programa:

int_v = []

cabecalho('Separar Par e Impar de um Vetor')
print()
tamanho = int(input('Qual o tamanho do Vetor: '))

print()

criaVet(int_v, tamanho, int)

print()
cabecalho('Resultados')

vet_print_par_or_impar(int_v)