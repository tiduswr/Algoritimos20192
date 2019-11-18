def criaVet(vet, tamanho):
    for i in range(tamanho):
        vet.append(0)
    return vet

def solic_val(vet, tamanho):
    for i in range(tamanho):
        vet[i] = input('Valor {}: '.format(i+1)).upper()
    return vet
    
def cabecalho(texto, largura):
    txt = str(texto)
    print('=' * largura)
    print('{:^{}}'.format(txt, largura))
    print('=' * largura)
    return

def verif_se_ordem(vet):
	for i in range(len(vet)):
		if vet[i] > vet[i+1]:
			print('A posição {} não esta em ordem!'.format(i+1))
			return
		else:
			print('Lista em Ordem!')
			return
#----------------------------------------------------------------
lista = []
cabecalho('Verifique se a lista esta em Ordem Crescente!', 50)
tamanho = int(input('\nQual o tamanho do Vetor? '))

criaVet(lista, tamanho)
print()

cabecalho('Solicitação de valores', 50)
print()
solic_val(lista, tamanho)
print()

cabecalho('Resultado', 50)
print()
verif_se_ordem(lista)