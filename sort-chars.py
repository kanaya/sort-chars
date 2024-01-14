import sys

with open(sys.argv[1]) as f:
	lines = f.read().splitlines()
	for line in lines:
		listified = list(set(list(line)))
		listified.sort()
		word = ''.join(listified)
		print(word)
