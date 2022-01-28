input1 = open("shivaram01.txt","r")  # open file, read-only
output = open("shivaram02.txt", "w") # open file, write
lines = input1.readlines()
lines.sort()

for line in lines:
	output.write(line)

input1.close()
output.close()
