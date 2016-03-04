f = open("input.txt", "r")
#opens file and reads in info

inputText = f.readlines()
#creates list with input contents
#makes a list of lines

f.close()
#closes input file

f = open("output.txt", "w")
#opes output file with no content

for line in inputText:
	#line represents each line in inputText
	if len(line) > 10:
		f.write(line[:10])
		#if line is more than 10 characters, it will write only the first 10 characters in the output file
		f.write("\n")
		#spaces the lines out properly
	else:
		f.write(line)
		#writes the regular line if it has 10 characters or less

f.close()
#closes output file