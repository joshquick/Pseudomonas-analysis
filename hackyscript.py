
from collections import defaultdict
import glob
import re

samples = defaultdict(list)
files = glob.glob("reads/*.gz")
for f in files:
	m = re.search(r'-(\d+)_', f)
	if m:
		samples[m.group(1)].append(f)
		samples[m.group(1)].sort()

for s, files in samples.iteritems():
	print """samtools merge - <(bwa mem reference/NC_002516.fasta %s %s | samtools view -bS -) <(bwa mem reference/NC_002516.fasta %s %s | samtools view -bS -) | samtools sort - alignments/%s_PAO1.sorted""" % (files[0], files[1], files[2], files[3], s)
