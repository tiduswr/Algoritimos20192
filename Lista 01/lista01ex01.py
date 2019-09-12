print('SIMULADOR DE COMPRA DE COMBUSTIVEL')
ValorGas = float(input('Insira o valor do Combustivel em "R$": '))
ValorPago = float(input('Quanto em "R$" você deseja abastecer? '))
ValorFinal = ValorPago / ValorGas
print('Você vai obter aproximadamente {:.0f}l de Combustivel!'.format(ValorFinal))