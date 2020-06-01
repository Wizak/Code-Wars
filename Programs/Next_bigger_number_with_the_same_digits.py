
def next_bigger(n):
	result = []
	def permutations(head, tail=''):
		nonlocal result

		if len(head) == 0:
			result.append(tail)
		else:
			for i in range(len(head)):
				permutations(head[0:i] + head[i+1:], tail+head[i])
	permutations(str(n))
	return int(''.join(list(result[1])))
if __name__ == '__main__':

	n = 2017

	print(next_bigger(n))