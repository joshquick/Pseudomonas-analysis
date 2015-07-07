from ete2 import NodeStyle, TreeStyle, Tree, TextFace
import sys
import csv

t = Tree(sys.argv[1])

R = t.get_midpoint_outgroup()
t.set_outgroup(R)

colours = {'X' : 'red', 'Y' : 'blue', 'Z': 'green', 'W' : 'yellow'}
#colours = {'CC-A' : 'red', 'CC-B' : 'blue', 'CC-C': 'green', 'CC-D' : 'yellow'}

samples = {}
with open(sys.argv[2]) as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		samples[row['IsolateID']] = row

# Basic tree style
ts = TreeStyle()
ts.show_leaf_name = True

ts.mode = "c"
#ts.arc_start = -180 # 0 degrees = 3 o'clock
#ts.arc_span = 180

nstyle = NodeStyle()
nstyle['shape'] = 'sphere'
nstyle['size'] = 4
nstyle['fgcolor'] = 'black'

for n in t.traverse():
	n.set_style(nstyle)

# Create an independent node style for each leaf, which
# specifies the colour given in the locations.csv file
for n in t.get_leaves():
	name = n.get_leaf_names()[0]
	print name
	nstyle = NodeStyle()
	try:
		nstyle["fgcolor"] = colours[samples[name]['Hospitals']]
#Hospitals']]
	except KeyError:
		nstyle["fgcolor"] = "grey"
	nstyle["size"] = 10

	n.set_style(nstyle)

	try:
		n.add_face(TextFace(samples[name]['Locations']), column=0, position = "branch-right")
	except:
		pass
	try:	
		n.add_face(TextFace(samples[name]['SamplingPeriod']), column=1, position = "branch-right")
	except:
		pass
t.render(file_name=sys.argv[3], tree_style=ts)

