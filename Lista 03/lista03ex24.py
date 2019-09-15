gabguard=''
maior=menor=ponttotal=countalun=0
print('='*50)
print('{: ^50}'.format('GABARITO'))
print('='*50)
for e in range(1,11):
    gabarito = input('{} - Digite o gabarito das notas: '.format(e)).upper()[0]
    gabguard = gabguard + gabarito
continuar = ''
while continuar != 'S':
    contacer = 0
    print('='*50)
    print('{: ^50}'.format('GABARITO ALUNO'))
    print('='*50)
    for f in range(1,11):
        gabaalun = input('{} - Digie a resposta: '.format(f)).upper()   
        if (f == 1 and gabaalun == gabguard[0]) or (f == 2 and gabaalun == gabguard[1]) or (f == 3 and gabaalun == gabguard[2]) or (f == 4 and gabaalun == gabguard[3]) or (f == 5 and gabaalun == gabguard[4]) or (f == 6 and gabaalun == gabguard[5]) or (f == 7 and gabaalun == gabguard[6]) or (f == 8 and gabaalun == gabguard[7]) or (f == 9 and gabaalun == gabguard[8]) or (f == 10 and gabaalun == gabguard[9]):
            contacer = contacer + 1
        if contacer > maior:
            maior = contacer
        if contacer < menor or contacer == 1:
            menor = contacer
    countalun = countalun + 1
    ponttotal = ponttotal + contacer
    continuar = input('\nDigite qualquer caractere para continuar\nou "S" Para sair: ').upper()
medalun = ponttotal // countalun
print('='*50)
print('{: ^50}'.format('RESULTADO'))
print('='*50)
print('Maior Acerto: ',maior)
print('Menor Acerto', menor)
print('Total de Alunos', countalun)
print('Média dos Alunos: ',medalun)