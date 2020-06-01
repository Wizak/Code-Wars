from time import sleep

def primeFactors(n):

	times, number = [], []
	i, t = 2, 1

	while t != n :
		i += 1

		if n%i == 0:
			number.append(i)
			times.append(n//i)

			for k, l in zip(number, times):
				t *= i*(n//i)

	return list(zip(number, times))

print(primeFactors(225))