def alphabet_position(text):
	return ' '.join([i for i in list(map(ord, text)) if i in range(ord('a'), ord('z')+1)])


if __name__ == '__main__':

	text = 'The sunset sets at twelve o\' clock.'
	print(list(map(ord, text)))

	try:
		print(alphabet_position(text))
	except:
		print('\n\nCatch error!')