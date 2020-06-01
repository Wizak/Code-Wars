def last_digit(n1, n2):

	N1 = {
		0:{i:0 for i in range(1,10)},
		1:{i:1 for i in range(1,10)}, 
		2:dict({i:2 for i in [1,5,9]}.items+{i:4 for i in [2,6]}.items+{i:6 for i in [4,8]}.items+{i:8 for i in [3,7]}.items), 
		}

	base = str(n1)[-1]
	power = str(n2)[-1]

	ask = N1[base][power]

	return ask


n1, n2 = 2, 1

print(last_digit(n1, n2))