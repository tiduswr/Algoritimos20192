salario = float(input('Valor do Salario: '))
despesas = float(input('Despesas mensais: '))
economia = salario - despesas
meses = 1000000 / economia
anos = meses // 12
print('São necessários {:.1f} anos para economizar R$ 1000000,00'.format(anos))
