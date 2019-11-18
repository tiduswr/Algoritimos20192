def primo(pval):
	for i in range(2,pval):
		if pval % i == 0:
			return False
	return True

n = int(input('Quantos Primos?'))

num = 2

while n > 0:
	if primo(num):
		print(num)
		n = n - 1
	num = num + 1