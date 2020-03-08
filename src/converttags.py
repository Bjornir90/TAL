import argparse

def getArgs():
	parser = argparse.ArgumentParser(description="Pos_tag text")
	parser.add_argument("in_file", help="The input file containing the text and the original tags")
	parser.add_argument("out_file", help="The output file containing the tokens with their corresponding tags")
	parser.add_argument("table_file", help="The file containing the correspondance between the two tags systems")
	return parser.parse_args()
	
args = getArgs()
in_file = open(args.in_file, "r")
table_file = open(args.table_file, "r")

default = "X"

dict = {}

for line in table_file:
	split = line.split()
	if split[0] == "DEFAULT":
		default = split[1]
		continue
	dict[split[0]] = split[1]
	
table_file.close()

result = ""

for line in in_file:
	if line == "\n":
		result += line
		continue
	
	if "\t" in line:
		split = line.split("\t")
	else:
	    split = line.split()
	
	#if there is multiple words on the same line, we need to split them up 
	if " " in split[0]:
		allWords = split[0].split()
		atFirstWord = True
		
		for word in allWords:
			newLabel = dict.get(split[1].rstrip(), default)
			if not atFirstWord:
				newLabel = newLabel.replace("B", "I")
			atFirstWord = False
			print("Label : "+newLabel)
			result += word + "\t" + newLabel + "\n"
		continue
		
		
	result += split[0] + "\t" + dict.get(split[1].rstrip(), default) + "\n"
 
in_file.close()

out_file = open(args.out_file, "w")

out_file.write(result)

out_file.close()
