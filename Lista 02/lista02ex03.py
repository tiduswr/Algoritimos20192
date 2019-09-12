print('Calculadora de notas! ')
n1 = float(input('Insira sua primeira nota: '))
n2 = float(input('Insira sua Segunda nota: '))
n3 = float(input('Insira sua Terceira nota: '))
media = (n1 + n2 + n3) / 3
if media >=7:
     print('Você esta Aprovado! ')
elif media >= 5 and media < 7:
     print('Você esta na final! ')
else:
	print('Reprovado!! ')