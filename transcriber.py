import sys

# Labeling a new dictionary that pairs characters to ipa
dict = {}

tagalog_ipa = open('tagalogipa.tsv', 'r')

# For each of the lines of input from the tsv file
for line in tagalog_ipa.readlines():
	# Strip any excess newlines
	line = line.strip('\n')
	# If there is no tab character, skip the line
	if '\t' not in line:
		continue
	# Split the values on the tab
	(t, i) = line.split('\t')
	dict[t] = i

# For each of the lines of input from the tokenizer.py file
for line in sys.stdin.readlines():
	# Strip excess newlines
	line = line.strip('\n')
	# If there is no tab character, skip the line
	if '\t' not in line:
		print(line)
		continue
	# Make a list of the cells in the row
	row = line.split('\t')
	# If there are not 10 cells, skip the line and keep going
	if len(row) != 10:
		continue
	# Name a new variable ipa as being the value of the input currently in position 1 in the row
	ipa = row[1]
	# Create a for loop to loop over each character "t" in the dictionary
	for t in dict:
		# Within the loop, take the predefined ipa (which was the tagalog word)
		# And then replace the character by the match in the dictionary.
		# This will loop over all characters in the word and replace them all
		# Storing them in the renamed ipa variable
		ipa = ipa.replace(t, dict[t])
		# Store the result of the ipa variable in the nineth spot in the row
	row[9] = 'ipa=%s' % (ipa)
	# Print the entire row
	print('\t'.join(row))
