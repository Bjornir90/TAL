import argparse

def getArgs():
	parser = argparse.ArgumentParser(description="Pos_tag text")
	parser.add_argument("in_file", help="The input file containing the text")
	parser.add_argument("out_file", help="The output file containing the text without empty lines")
	return parser.parse_args()
	
args = getArgs()

file = open(args.in_file, "r")

result = ""

for line in file:
	if line is "\n":
		continue
	result += line
	
file.close()

file = open(args.out_file, "w") 
file.write(result)
file.close()