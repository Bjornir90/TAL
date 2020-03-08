import argparse

def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("conv_table", help="File containing the matching tags between PTB and univ")
	parser.add_argument("fin", help="Reference text file (with tags in it)")
	parser.add_argument("fout", help="Output file")
	return parser.parse_args()
	
args = get_args()

match_table = open(args.conv_table, 'r')

match_dict = {}

for line in match_table:
	if line[-1] == '\n':
		line = line[:-1]
	split_line = line.split(" ")
	while "" in split_line:
		split_line.remove("")
	print(split_line)
	match_dict[split_line[0]] = split_line[1]

match_table.close()
#print(match_dict)

ref_ptb = open(args.fin, 'r')
result_file = open(args.fout, 'w')

for line in ref_ptb:
	if line[-1]=="\n":
		line = line[:-1]
	splitted_line = line.split(" ")
	result = ""
	for elt in splitted_line:
		splitted_elt = elt.split("_")
		if not match_dict.has_key(splitted_elt[1]):
			match_dict[splitted_elt[1]] = "None"
		result += splitted_elt[0] + "\t" + match_dict[splitted_elt[1]] + "\n"
	result_file.write(result[:-1]+"\n")
		
ref_ptb.close()
result_file.close()
