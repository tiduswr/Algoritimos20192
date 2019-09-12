print('MÉDIA DE CONSUMO DE COMBUSTIVEL DE UM VEICULO')
km_ini = float(input('Informe a Quilometragem inicial mostrada no contador do veiculo: '))
km_end = float(input('Informe a Quilometragem final mostrada no contador do veiculo: '))
km_perc = km_end - km_ini
gas_gast = float(input('Insira quantos litros foram gastos no percurso: '))
gas_por_km = km_perc / gas_gast
print('A cada 1l de combustivel gasto, você percorreu {:.1f}km.'.format(gas_por_km))