import vcf
import sys

for pos in vcf.Reader(open(sys.argv[1], 'r')):
	if pos.is_indel:
		print pos.POS, "indel"

