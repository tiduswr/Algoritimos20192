massa = float(input('Massa: '))
print('Massa Inicial: ',massa)
cont = 0
while massa > 0.5:
	massa = massa / 2
	cont = cont + 50
print('Massa Final: ',massa)
print('Tempo necessario: ',cont)