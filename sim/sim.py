import random

a_file = open('bowl.csv', "r")
bowl_list = []
for line in a_file:
	line = line.strip("\n")
	word = line.split(",")
	bowl_list.append(word)

b_file = open('bat.csv', "r")
bat_list = []
for line in b_file:
	line = line.strip("\n")
	word = line.split(",")
	bat_list.append(word)
#print(main_list)
#print(bat_list)
#print(bowl_list)
team_a = []
team_b = []

def search(my_list, a):
	res = False
	for i in my_list:
		if(i[0]==a):
			res = True
	return res

def in_team():
	print("Enter the players of team 1 in the batting order")
	for i in range(0,11):
		x = input()
		if(search(bat_list, x)==True):
			team_a.append(x)
		else:
			print("Batsman",x,"not in list. Using Luke Wright instead.")
			team_a.append("Luke Wright")
	#team_b = []
	print("Enter the players of team 2 in the bowling order")
	for i in range(0,20):
		x = input()
		if(search(bowl_list, x)==True):
			team_b.append(x)
		else:
			print("Bowler", x, "not in list. Using HV Patel instead")
			team_b.append("HV Patel")

a_file = open('result_cum.csv', "r")
prob_cum = []
for line in a_file:
	line = line.strip("\n")
	word = line.split(",")
	prob_cum.append(word)
#print(prob_cum)
prob_cum = prob_cum[1:]
def find_bat_cluster(a):
	x = -1
	for i in bat_list:
		if(a==i[0]):
			x = i[1]
	return x

def find_bowl_cluster(a):
	x = -1
	for i in bowl_list:
		if(a==i[0]):
			x = i[1]
	return x

c_file = open('wicket.csv', "r")
wickets = []
for line in c_file:
	line = line.strip("\n")
	word = line.split(",")
	wickets.append(word)
wickets = wickets[1:]
##print(wickets)

def sim():
	runs = 0
	m = 0
	q = 0
	prob = 1
	balls = 0
	for i in range(0,120):
		balls = balls+1
		batsman = team_a[m]
		bowler = team_b[q]
		batc = find_bat_cluster(batsman)
		bowlc = find_bowl_cluster(bowler)
		#print(batc)
		#print(bowlc)
		print(batsman)
		print(bowler)
		cum_zero = -1
		cum_one = -1
		cum_two = -1
		cum_three = -1
		cum_four = -1
		cum_six = -1
		num = random.uniform(0,1)
		print("Num: ", num)
		for j in prob_cum:
			if (j[0]==batc and j[1]==bowlc):
				cum_zero = float(j[2])
				cum_one = float(j[3])
				cum_two = float(j[4])
				cum_three = float(j[5])
				cum_four = float(j[6])
				cum_six = float(j[7])
		#print(cum_zero, cum_one, cum_two, cum_three, cum_four, cum_six)
		if(num >= 0 and num <= cum_zero):
			runs = runs + 0
			print("zero")
		elif(num > cum_zero and num <=cum_one):
			runs = runs + 1
			print("One")
		elif(num > cum_one and num <=cum_two):
			runs = runs + 2
			print("two")
		elif(num > cum_two and num <=cum_three):
			runs = runs + 3
			print("three")
		elif(num > cum_three and num <=cum_four):
			runs = runs + 4
			print("four")
		elif(num > cum_four and num <=cum_six):
			runs = runs + 6
			print("six")
		print("Runs: ", runs)
		for k in wickets:
			if(k[0]==batc and k[1]==bowlc):
				prob = prob * 1-float(k[2])
		print("Prob of not getting out: ", prob)
		if(prob <= 0.5):
			print("BATSMAN GETS OUT!")
			if(m < 10):
				m = m + 1
				prob = 1
			else:
				('Team bowled out')
		if(balls == 6):
			q = q + 1
			balls = 0

		





in_team()
#print(team_a)
#print(team_b)
sim()