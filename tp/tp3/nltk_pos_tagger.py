import nltk
from nltk.tokenize import word_tokenize
import argparse

def getArgs():
    parser = argparse.ArgumentParser(description="Pos_tag text")
    parser.add_argument("in_file", help="The input file containing the text to pos_tag")
    parser.add_argument("out_file", help="The output file containing the tokens with their tag")
    return parser.parse_args()

args = getArgs()
file = open(args.in_file, "r")

res = []

for line in file:
    l = nltk.pos_tag(word_tokenize(line))
    for token in l:
        if token[0] == '``':
            res.append(token[0]+"\t.\n")
        else:
            res.append(token[0]+"\t"+token[1]+"\n")

file.close()

file = open(args.out_file, "w")
file.writelines(res)
file.close()