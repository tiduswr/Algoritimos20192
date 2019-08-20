print('====Calculo de multa por atraso====')
print('Favor, utilizar apenas numeros para preencher.')
valini_div = float(input('*Digite o valor inicial da divida: '))
dias_atraso = float(input('*Quantos dias de atraso na divida se passaram? ' ))
taxa_atraso = float(input('*Digite o valor da Multa por dia de atraso: '))
tax_atr_fin = dias_atraso * taxa_atraso
multa_tot = tax_atr_fin + valini_div
print('De acordo com os dias de atraso e taxa de multa diaria informada,\n a multa total esta avaliada em R$ {:.2f}'.format(multa_tot))