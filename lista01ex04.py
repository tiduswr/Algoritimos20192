print('CALCULO DE AREA TOTAL DE UMA CASA EM M²(Máximo de 4 Comodos)')
ComC1 = float(input('Insira o Comprimento do Primeiro Comodo: '))
ComL1 = float(input('Insira a Largura do Primeiro Comodo: '))
Area1 = ComC1 * ComL1
print('A area do primeiro comodo é igual a: {}' .format(Area1))
ComC2 = float(input('Insira o Comprimento do Segundo Comodo: '))
ComL2 = float(input('Insira a Largura do Segundo Comodo: '))
Area2 = ComC2 * ComL2
print('A area do segundo comodo é igual a: {}' .format(Area2))
ComC3 = float(input('Insira o Comprimento do Terceiro Comodo: '))
ComL3 = float(input('Insira a Largura do Terceiro Comodo: '))
Area3 = ComC3 * ComL3
print('A area do terceiro comodo é igual a: {}' .format(Area3))
ComC4 = float(input('Insira o Comprimento do Quarto Comodo: '))
ComL4 = float(input('Insira a Largura do Quarto Comodo: '))
Area4 = ComC4 * ComL4
print('A area do quarto comodo é igual a: {}' .format(Area4))
AreaCasa = Area1 + Area2 + Area3 + Area4
print('A area em m² da casa informada é de {}.'.format(AreaCasa))