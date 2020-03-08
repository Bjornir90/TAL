import argparse

def getArgs():
	parser = argparse.ArgumentParser(description="Pos_tag text")
	parser.add_argument("in_file", help="The input file containing the text and the original tags")
	parser.add_argument("out_file", help="The output file containing the tokens without their corresponding tags")
	return parser.parse_args()
	
args = getArgs()
in_file = open(args.in_file, "r")

result = ""

for line in in_file:
	if line == "\n":
		result += line
		continue
	if "\t" in line:
		split = line.split("\t")
	else:
	    split = line.split()
	result += split[0] + " "
	
in_file.close()

out_file = open(args.out_file, "w")

out_file.write(result)

out_file.close()