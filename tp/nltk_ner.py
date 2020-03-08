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

out_file = open(args.out_file, "w")

for chunk in named:
	if hasattr(chunk, "label"):
		out_file.write("".join(c[0] for c in chunk)+"\t"+chunk.label()+"\n")


out_file.close()