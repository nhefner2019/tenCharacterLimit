f = open("input.txt", "r")

inputText = f.readlines()

f.close()

f = open("output.txt", "w")

for word in inputText:
	if len(word) > 10:
		f.write(word[:10])
		f.write("\n")
	else:
		f.write(word)

f.close()