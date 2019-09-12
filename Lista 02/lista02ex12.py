print('Saiba as Centenas, Dezenas e Unidades de um numero menor\nque 1000 e maior que 0 \n\n*Por favor, digite somente numeros INTEIROS!\n\n')
#Ajustando uma condição em que o usuario insira um numero como foi pedido:
num = int(input('Digite um numero: '))
while num < 0 or num >= 1000:
	num = int(input('Por favor, digite um numero maior que zero e menor que\nmil!!: '))
#Separando as Unidades, Dezenas e Centenas:
cent = num // 100
dez = (num % 100) // 10
und = (num % 100) % 10
#Nomeando as variaveis de ligação:
ligcd = ''
ligcu = ''
ligdu = ''
#Estabelecendo condições para as variaveis de ligação:
if cent >=1 and dez >= 1 and und == 0:
	ligcd = ' e '
if cent >= 1 and und >= 1 and dez == 0:
	ligcu = ' e '
if cent >= 1 and dez >= 1 and und >= 1:
	ligcd=', '
	ligcu = ' e '
if cent == 0 and dez >= 1 and und >= 1:
	ligdu = ' e '
#Estabelecendo condições para variaveis de nomenclatura com relação ao plural ou se uma das 3 casas estão zeradas:
if cent > 1:
	c = ' Centenas'
elif cent == 1:
	c = ' Centena'
elif cent == 0:
	c = ''
	cent = ''
if dez > 1:
	d = ' Dezenas'
elif dez == 1:
	d = ' Dezena'
elif dez == 0:
	d = ''
	dez = ''
if und > 1:
	u = ' Unidades'
elif und == 1:
	u = ' Unidade'
elif und == 0:
	u = ''
	und= ''
#Resultado:
print(('\nSeu numero possui {}{}{}{}{}{}{}{}{}.\n\nObrigado por usar o programa! :)').format(cent,c,ligcd,dez,d,ligcu,ligdu,und,u))