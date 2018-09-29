import csv
def my_join(f1,f2):
	f3=open(f1,'r')
	f4=open(f2,'r')
	file1=f3.readlines()
	file2=f4.readlines()
	p1 = [] #names
	p2 = [] #clusters
	for i in file1:
		l1=i.strip('\n').split("::::")
		p1.append(l1)
	
	for i in file2:
		l2=i.strip('\n').split(",")
		p2.append(l2)

	for j in p2:
		for i in p1:
			if i[1] == j[0]:
				j.append(i[0])
	out = csv.writer(open("all_com_final.csv","w"), delimiter=',',quoting=csv.QUOTE_ALL)
	for i in p2:
		out.writerow(i)
my_join("matched_batsmen_profile2.txt", "all_combined.csv")