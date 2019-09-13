qtdcdd = soma = somaacid = maior = menor = count = 0
print('='*50)
print('{:.^50}'.format('PESQUISA ESTATISTICA - ACIDENTE NO TRANSITO!'))
print('='*50)
qtdcdd = int(input('Quantidade de Cidades para o teste: '))
for i in range (1,qtdcdd+1):
    print('='*50)
    cddname = input('Nome da cidade: ')
    codcddi = int(input('Código da cidade: '))
    numvei = int(input('Número de veículos de passeio: '))
    numacid = int(input('Numero de acidentes de trânsito com vitimas: '))
    soma = soma + numvei
    if numvei <= 2000:
        somaacid = somaacid + numacid
        count = count + 1
    if numacid > maior:
        maior = numacid
        nommaior = cddname
    if numacid < menor or i == 1:
        menor = numacid
        nommenor = cddname
mediavei = soma / qtdcdd
if somaacid > 0:
    somaacid = somaacid / count
print('='*50)
print('Resultados da pesquisa:\nMaior Indice de Acidentes: {} - {}\nMenor Indice de Acidentes: {} - {}\nMédia de veiculos nas {} cidades: {}'.format(maior,nommaior,menor,nommenor,qtdcdd,mediavei))
if somaacid > 0:
    print('Média de acidentes em cidades com menos de 2000 veiculos: {}'.format(somaacid))  