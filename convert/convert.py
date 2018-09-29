a_file = open('match.txt', "r")
bat_list = []
for line in a_file:
	line = line.strip("\n")
	word = line.split("::::")
	bat_list.append(word)

def search(my_list, a):
	res = "Not found"
	for i in my_list:
		if(i[0]==a):
			res = i[1]
	return res

for i in range(0,11):
	x = input()
	print(search(bat_list, x))
