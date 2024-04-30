import sys

line = sys.stdin.readline()

abbrev = ("cit.")
url = ("www.")


while line:
	for token in line.strip().split(' '):
		if not token:
			continue
		if token[-1] in '!?':
			sys.stdout.write(token + '\n')
		elif token[-1] == '.':
			if token in ['etc.', 'i.e.', 'e.g.']:
				sys.stdout.write(token + ' ')
			else:
				sys.stdout.write(token + '\n')
		else:
			sys.stdout.write(token + ' ')
	line = sys.stdin.readline()
