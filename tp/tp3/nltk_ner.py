import nltk

import argparse

def getArgs():
	parser = argparse.ArgumentParser(description="Pos_tag text")
	parser.add_argument("in_file", help="The input file containing the text to perform NER on")
	parser.add_argument("out_file", help="The output file containing the tokens with their tag")
	return parser.parse_args()

args = getArgs()

in_file = open(args.in_file, "r")

#print(nltk.pos_tag(nltk.word_tokenize(in_file.read())))

taggedList = []

for line in in_file:
	tagged = nltk.pos_tag(nltk.word_tokenize(line))
	for elem in tagged:
		taggedList.append(elem)

in_file.close()

named = nltk.ne_chunk(taggedList, binary=False)

print(named)

out_file = open(args.out_file, "w")

for chunk in named:
	print(chunck)
	if hasattr(chunk, "label"):
	
		atStartOfChunk = True
		#Put a space in-between words composing a multi-word entity name
		for c in chunk:
			if not atStartOfChunk:
				out_file.write(" ")
			out_file.write(c[0])
			atStartOfChunk = False
			
		out_file.write("\t"+chunk.label()+"\n")
	else:
		out_file.write("".join(chunk[0])+"\tO\n")

out_file.close()
