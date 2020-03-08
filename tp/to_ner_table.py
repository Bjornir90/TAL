from __future__ import division
import argparse

def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("ner_output_file", help="Output file of your NER tool (John/PERSON ate/O etc...)")
	return parser.parse_args()

ner_file = open(get_args().ner_output_file)

entity_dict = {}
type_dict = {}

for line in ner_file:
	if line[-1] == "\n":
		line = line[:-1]
	splitted = line.split(" ")
	for elt in splitted:
		splitted_elt = elt.split("/")
		print(splitted_elt)
		if(not len(splitted_elt)==2):
			continue
		if entity_dict.has_key(splitted_elt[0]):
			entity_dict[splitted_elt[0]][1] += 1
			type_dict[splitted_elt[1]] += 1
		else:
			entity_dict[splitted_elt[0]] = [splitted_elt[1], 1]
			if type_dict.has_key(splitted_elt[1]):
				type_dict[splitted_elt[1]] += 1
			else:
				type_dict[splitted_elt[1]] = 1

ner_file.close()

## Output file building

def write_formatted_line(file_to_write_in):
	line = named_entity + (20 - len(named_entity)) * " "
	line += ent_type + (10 - len(ent_type)) * " "
	line += occurence + (10 - len(occurence)) * " "
	line += rate
	file_to_write_in.write(line + "\n")

named_entity = "Entite nommee"
ent_type = "Type"
occurence = "Nombre d'occurences"
rate = "Proportion dans le texte(%)"

# Init file

output = open(get_args().ner_output_file + ".table", "w")
write_formatted_line(output)

# Write results in the output

for entity in entity_dict:
	ent_type = entity_dict[entity][0]
	if ent_type == "O":
		continue
	named_entity = entity
	occurence = str(entity_dict[entity][1])
	rate = str(entity_dict[entity][1]/type_dict[ent_type]*100) + "(" + str(entity_dict[entity][1]) + "/" + str(type_dict[ent_type]) + ")"
	write_formatted_line(output) 
	




