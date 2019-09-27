#Solicite ao usuario a informação do nome de Diversos Alunos e a média de cada um deles. Para encerrar, o usuario deve digitar 'Fim'. Informe: Alunos Aprovados, Alunos na Final e Alunos Reprovados.
alunos = []
notas = []
nome = input('Nome do aluno: ')
while nome != 'fim':
	alunos.append(nome)
	nota = float(input('Média: '))
	notas.append(nota)
	nome = input('Nome do aluno: ')
print('Alunos Aprovados: ')
for i in range(len(notas)):
	if notas[i] >= 7:
		print(alunos[i])
print('Alunos na Final: ')
for i in range(len(notas)):
	if notas[i] >= 4 and notas[i] < 7:
		print(alunos[i])
print('Alunos Reprovados: ')
for i in range(len(notas)):
	if notas[i] < 4:
		print(alunos[i])