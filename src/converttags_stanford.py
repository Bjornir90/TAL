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

dict = {}

for line in table_file:
    split = line.split()
    dict[split[0]] = split[1]
	
table_file.close()

result = ""

for line in in_file:
    if line == "\n":
        result += line
        continue
    split = line.split("\t")
    #if split[1].rstrip() in dict:
    result += split[0] + "\t" + dict.get(split[1].rstrip(), "X") + "\n"
    #else:
        #result += split[0] + "\tX\n"
 
in_file.close()

out_file = open(args.out_file, "w")

out_file.write(result)

out_file.close()
