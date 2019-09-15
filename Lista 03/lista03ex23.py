print('-'*79)
print('{:=^79}'.format('SAIBA SUA DIVIDA AQUI!'))
print('-'*79)
div = float(input('Insira sua divida: '))
jur1=jur3=jur6=jur9=jur12=0
print('\nSegue tabela abaixo:\n\n')
valparc1=valparc3=valparc6=valparc9=valparc12=0
for parc in range(1,13,1):
    if parc == 1:
        jur1 = 0
        parc1 = 1
        div1 = div + jur1
        valparc1 = div1 / 1
    elif parc == 3:
        jur3 = div * (10/100)
        div3 = div + jur3
        parc3 = 3
        valparc3 = div3 / 3
    elif parc == 6:
        jur6 = div * (15/100)
        div6 = div + jur6
        parc6 = 6
        valparc6 = div6 / 6
    elif parc == 9:
        jur9 = div * (20/100)
        div9 = div + jur9
        parc9 = 9
        valparc9 = div9 / 9
    elif parc == 12:
        jur12 = div * (25/100)
        div12 = div + jur12
        valparc12 = div12 / 12
        parc12 = 12
print('Valor da Divida | Valor dos Juros | Quantidade de Parcelas | Valor da Parcela |')
print('-'*79)
print('R$ {:^13.2f}|'.format(div1),'R$ {:^13.2f}|'.format(jur1),'{:^23}|'.format(parc1),'R$ {:^14.2f}|'.format(valparc1))
print('R$ {:^13.2f}|'.format(div3),'R$ {:^13.2f}|'.format(jur3),'{:^23}|'.format(parc3),'R$ {:^14.2f}|'.format(valparc3))
print('R$ {:^13.2f}|'.format(div6),'R$ {:^13.2f}|'.format(jur6),'{:^23}|'.format(parc6),'R$ {:^14.2f}|'.format(valparc6))
print('R$ {:^13.2f}|'.format(div9),'R$ {:^13.2f}|'.format(jur9),'{:^23}|'.format(parc9),'R$ {:^14.2f}|'.format(valparc9))
print('R$ {:^13.2f}|'.format(div12),'R$ {:^13.2f}|'.format(jur12),'{:^23}|'.format(parc12),'R$ {:^14.2f}|'.format(valparc12))