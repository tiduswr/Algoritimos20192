print('='*50)
print('{:^50}'.format("Verificador de Acertos"))
print('='*50)
quest = 10
gab = [' ']*quest
aln = [' ']*quest
print('{:=^50}'.format('Insira o Gabarito'))
print()
for i in range (10):
	gab[i] = input('Questão {}: '.format(i+1)).upper()
	while gab[i] != 'A' and gab[i] != 'B' and gab[i] != 'C' and gab[i] != 'D' and gab[i] != 'E':
		gab[i] = input('Por Favor, insira somente letras entre "A" e "E"\nQuestão {}: '.format(i+1)).upper()
print()
print('{:=^50}'.format('Quantos alunos serão verificado? '))
qtdaln = int(input('Alunos: '))
acrturma = [' ']*qtdaln
for j in range(qtdaln):
	print('\n*****Insira as Respostas do Aluno {}'.format(j+1))
	acerto = 0
	for l in range (10):
		aln[l] = input('Questão {}: '.format(l+1)).upper()
		while aln[l] != 'A' and aln[l] != 'B' and aln[l] != 'C' and aln[l] != 'D' and aln[l] != 'E':
			aln[l] = input('Por Favor, insira somente letras entre "A" e "E"\nQuestão {}: '.format(l+1)).upper()
		if aln[l] == gab[l]:
			acerto = acerto + 1
			acrturma[j] = acerto
print()
print('{:=^50}'.format('Tabela de Acertos por Aluno'))
for m in range(qtdaln):
	print('Acertos do {}° Aluno: {} '.format(m+1, acrturma[m]))