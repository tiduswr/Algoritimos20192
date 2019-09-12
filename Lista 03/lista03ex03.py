pA = 80000
pB = 200000
anos = 0
while pA < pB:
	pA = (pA * (0.03)) + pA
	pB = (pB * (1.5/100)) + pB
	anos = anos + 1
print('As populações iram se igualar em {} anos.'.format(anos))