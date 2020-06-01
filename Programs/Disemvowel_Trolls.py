def disemvowel(string):
	f = lambda x: 0 if x in 'aeiouAEIOU' else 1
	return ''.join(list(filter(f, string)))

string = 'This website is for losers LOL!'
print(disemvowel(string))