print('SAIBA A MÉDIAS DE PESSOAS POR TURMA!\n\n*As turmas não podem conter mais que 40 alunos!\n')
turmas = int(input('Favor insira o numero de turmas: '))
print('')
alun = int(input('Insira a quantidade de alunos da primeira turma: '))
while alun > 40:
	alun = int(input('Por favor, não pode haver um numero maior de 40 alunos\npor turma, insira o valor novamente: '))	
soma = alun
for i in range(turmas-1):
	alun = int(input('Insira a quantidade de alunos da outra turma: '))
	while alun > 40:
		alun = int(input('Por favor, não pode haver um numero maior de 40 alunos\npor turma, insira o valor novamente: '))
	soma = soma + alun
media = soma / turmas
print('\nA média de alunos por turma é:',media)