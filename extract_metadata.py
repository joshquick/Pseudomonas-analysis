import sys

for line in open(sys.argv[1], 'r').readlines():
	cols = line.strip().split(',')
	if cols[8]:
		print ','.join([cols[8], cols[0], cols[1], cols[2], cols[3], cols [4]])
