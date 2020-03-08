import argparse

def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("fin", help="Input file containing a text with the NE tags")
	parser.add_argument("fout", help="Output file containing the same text in the right format")
	return parser.parse_args()
	
args = get_args()

fin = open(args.fin, "r")
fout = open(args.fout, "w")

for line in fin:
	result = ""
	if line[-1]=="\n":
		line=line[:-1]
	splitted = line.split(" ")
	for elt in splitted:
		splitted_elt = elt.split("/")
		if not len(splitted_elt)==2:
			continue
		print(splitted_elt)
		result += splitted_elt[0] + "\t" + splitted_elt[1] + "\n"
	fout.write(result + "\n")

fin.close()
fout.close()
