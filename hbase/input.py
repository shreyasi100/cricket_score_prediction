a_file = open('result.csv', "r")
main_list = []
for line in a_file:
	line = line.strip("\n")
	word = line.split(",")
	main_list.append(word)
#print(main_list)
l = len(main_list)
for i in range(0,l):
	print("put 'prob2', ","'",i,"', 'id:id',","'",main_list[i][0],"'", sep='')
	print("put 'prob2', ","'",i,"', 'bat_cluster:bat_cluster',","'",main_list[i][1],"'", sep='')
	print("put 'prob2', ","'",i,"', 'bowl_clutser:bowl_cluster',","'",main_list[i][2],"'", sep='')
	print("put 'prob2', ","'",i,"', 'zero:zero',","'",main_list[i][3],"'", sep='')
	print("put 'prob2', ","'",i,"', 'one:one',","'",main_list[i][4],"'", sep='')
	print("put 'prob2', ","'",i,"', 'two:two',","'",main_list[i][5],"'", sep='')
	print("put 'prob2', ","'",i,"', 'three:three',","'",main_list[i][6],"'", sep='')
	print("put 'prob2', ","'",i,"', 'four:four',","'",main_list[i][7],"'", sep='')
	print("put 'prob2', ","'",i,"', 'six:six',","'",main_list[i][8],"'", sep='')
	print("put 'prob2', ","'",i,"', 'no_of_balls: no_of_balls',","'",main_list[i][9],"'", sep='')