#Uma empresa possui N funcionarios. Leia nomes, cargos e salarios destes funcionarios e imprima a folha salarial dando um aumento de 20% para os gerentes.
n = int(input('Quantos Funcionarios? '))
nomes = [' '] * n
cargos = [' '] * n
salarios = [0] * n
for i in range(n):
	nomes[i] = input('Nomes: ')
	cargos[i] = input('Cargo: ')
	salarios[i] = float(input('Salarios: '))
for i in range(n):
	if cargos == 'Gerente':
		print(nomes[i], cargos[i], salarios[i]*1.2)
	else:
		print(nomes[i], cargos[i], salarios[i])
