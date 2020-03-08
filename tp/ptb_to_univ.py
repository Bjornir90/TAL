

match_table = open("POSTags_PTB_Universal_Linux.txt", 'r')

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
print(match_dict)

ref_ptb = open("wsj_0010_sentence.pos.ref", 'r')
text = ref_ptb.read()

splitted_text = text.split(" ")
result = ""

for elt in splitted_text:
	splitted_elt = elt.split("_")
	result += splitted_elt[0] + "_" + match_dict[splitted_elt[1]] + " "

ref_ptb.close()

result_file = open("wsj_0010_sample.txt.pos.univ.ref", 'w')
result_file.write(result[:-1])
result_file.close()
