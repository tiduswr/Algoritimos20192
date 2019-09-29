#Leia uma sequencia de nomes, onde "Fim" é usado para finalizar a Sequência imprima duas listas numeradas com esses nomes uma na ordem de inserção e outra em ordem alfabética.
nomes = []
nome = input('Primeiro Nome: ')
while nome != 'Fim' and nome != 'fim' and nome != 'FIM':
	nomes.append(nome)
	nome = input('Outro Nome: ')
for i in range (1,len(nomes)+1,1):
	print(i,':',nomes[i-1])
nomes.sort()
for i in range (1,len(nomes)+1,1):
	print(i,':',nomes[i-1])