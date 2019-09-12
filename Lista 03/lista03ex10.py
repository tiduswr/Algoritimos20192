print("Informe os numeros inteiros para o calculo: \n")
base = int(input("Base: "))
exp = int(input("Expoente: "))
result = 1
for i in range(exp):
    result = result * base
print('\nO resultado é:\n\n{} ^({}) = {}'.format(base,exp,result))