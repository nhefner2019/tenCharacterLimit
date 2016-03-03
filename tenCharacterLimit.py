f = open("input.txt", "r")

inputText = f.readlines()

f.close()

f = open("output.txt", "w")

for word in inputText:
	f.write(word)

f.close()