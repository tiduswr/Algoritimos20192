print('QUANTAS CADEIRAS CABEM NA SALA')
comsala = float(input('Digite o comprimento da sala de aula: '))
larsala = float(input('Digite a largura da sala: '))
msala = comsala * larsala
comcad = float(input('Digite o comprimento de uma das cadeira: '))
larcad = float(input('Digite a largura de uma das cadeiras: '))
mcad = comcad * larcad
mareaprof = msala - 1.5
mareacad = mcad + (0.7 * 0.2)
cadtotal = mareaprof / mareacad
print('Você conseguira organizar um total de {:.0f} \n cadeira no espaço dessa sala de aula!'.format(cadtotal))