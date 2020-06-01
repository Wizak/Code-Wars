n = 2
m = 1

for k in range(2, n+1):
	m *= (n+k)/k

return int(m)
print(m)