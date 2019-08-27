print('Calculo de descontos no Salario bruto\n----------------------------------------------------')
hrs = float(input('Insira quantas horas você trabalhou: '))
vlr = float(input('Insira o valor da sua hora: '))
hrsttl = vlr * hrs
print('Salario Bruto: (R$ {:.2f} * {:.0f}hrs) : R$ {:.2f}'.format(vlr, hrs, hrsttl))
if hrsttl <= 900:
	ir = 0
	print('(-) IR (Isento) : R$ 0,00 ')
if hrsttl > 900 and hrsttl <= 1500:
	ir = hrsttl * (5/100)
	print('(-) IR (5%) : R$ {:.2f} '.format(ir))
if hrsttl > 1500 and hrsttl <= 2500:
	ir = hrsttl * (10/100)
	print('(-) IR (10%) : R$ {:.2f} '.format(ir))
if hrsttl > 2500:
	ir = hrsttl * (20/100)
	print('(-) IR (20%) : R$ {:.2f} '.format(ir))
sind =hrsttl * (3/100)
inss = hrsttl * (10/100)
fgts = hrsttl * (11/100)
print('(-) Sindicato : (3%) : R$ {:.2f}'.format(sind))
print('(-) INSS : (10%) : R$ {:.2f}'.format(inss))
print('FGTS : (11%) : R$ {:.2f}'.format(sind))
salliq = hrsttl - sind - inss - ir
print('Salario Liquido : R$ {:.2f} '.format(salliq))



