FILENAME = "1.txt"

file = open(FILENAME,"r")
all_date = file.readlines()

for item in all_date:
	print (item.strip()) 