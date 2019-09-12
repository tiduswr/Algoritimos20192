print('VERIFICAÇÃO DE TRIANGULOS')
a = int(input('Primeiro lado: '))
b = int(input('Segundo lado: '))
c = int(input('Terceiro lado: '))
if a + b <= c or b + c <= a or a + c <= b:
	print('Os valores informados não formam um triângulo! ')
elif a == b and b == c:
	print('Triangulo Equilatero!')
elif a != b and b != c and a != c:
	print('Triangulo escaleno!')
else:
	print('Triângulo isóceles! ')