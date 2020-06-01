def josephus(items,k):
	n = -1
	a = []

	while len(items) != len(a):
		n += k

		if n>=len(items):
			n -= len(items)
			a.append(items[n])
		else: 
			a.append(items[n])

		print(n)
		print(a)

	return a

if __name__ == '__main__':

	items = range(1, 11)
	k = 2

	print(josephus(items, k))