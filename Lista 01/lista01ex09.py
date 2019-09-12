print('CALCULADORA DE IDADE!')
nome = input('Insira seu nome: ')
print('Olá {}! Vou começar te pedindo uns dados. '.format(nome))
ano = int(input('Insira seu ano de Nascimento: '))
anoatual = int(input('Insira o ano atual: '))
idade = anoatual - ano
print('Bem {}, pelo que vi você tem {} anos de idade.'.format(nome, idade))