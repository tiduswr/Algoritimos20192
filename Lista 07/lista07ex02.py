#Funções:

def criaVet(vet, tamanho):
    for i in range(tamanho):
        vet.append(0)
    return vet

def solic_val(vet, tamanho, func):
    for i in range(tamanho):
        vet[i] = func(input('Questão {}: '.format(i+1))).upper()
    return vet

def ver_gab(tamanho, gab_alun, gab_prova, vet_acert):
    for i in range(tamanho):
        if gab_alun[i] == gab_prova[i]:
            vet_acert[i] = True
        else:
            vet_acert[i] = False
    return vet_acert

def porc_acert(tamanho, vet_acert):
    acertos = 0
    for i in range(tamanho):
        if vet_acert[i] == True:
            acertos = acertos + 1
    porcentagem = (acertos / tamanho) * 100
    return porcentagem

def cabecalho(texto):
    txt = str(texto)
    print('=' * 50)
    print('{:^50}'.format(txt))
    print('=' * 50)
    return
#------------------------------------------------------------------------------------
#Programa:

cand_gab = []
gab_ofi = []
cand_acert = []

cabecalho('Saiba quanto você acertou da Prova!')

tamanho = int(input('\nQuantas questões tem a prova? '))

gab_ofi = criaVet(gab_ofi,tamanho)
cand_acert = criaVet(cand_acert,tamanho)
cand_gab = criaVet(cand_gab,tamanho)

cabecalho('Insira o Gabarito da Prova')

gab_ofi = solic_val(gab_ofi,tamanho,str)

cabecalho('Insira o seu Gabarito')

cand_gab = solic_val(cand_gab,tamanho,str)

cand_acert = ver_gab(tamanho, cand_gab, gab_ofi, cand_acert)

cabecalho('RESULTADO')

print('Você acertou {:.0f}{} da Prova!'.format(porc_acert(tamanho, cand_acert), '%'))