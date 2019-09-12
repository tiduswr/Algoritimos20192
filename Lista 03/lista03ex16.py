numpess = int(input('Saiba quantas pessoas você deseja registrar as idades? '))
cont = 0
for i in range(numpess):
	idade = int(input('Insira a idade: '))
	cont = cont + idade
	media = cont / numpess
if media > 0 and media <= 25:
	print('A faixa etaria das idades informadas é de 0 a 25 anos,\nsendo enquadrado no grupo Jovens.')
if media > 26 and media <= 60:
	print('A faixa etaria das idades informadas é de 26 a 60 anos,\nsendo enquadrado no grupo Adultos.')
if media > 60:
	print('A faixa etaria das idades informadas é maior de 60 anos,\nsendo enquadrado no grupo Idosos.')