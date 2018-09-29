import os
def prob(f1,f2,f3):
        bat_cluster=os.listdir(f2)
        os.chdir(f2)
        list_of_bat=[]
        list_of_bowl=[]
        for i in bat_cluster:
               lines=open(i).readlines()
               s=[]
               for j in lines:
                      p=j.strip('\n').split(',')
                      if len(p) >13:
                        s.append(p[14])
               if s:
                 list_of_bat.append(s)
        print(list_of_bat)
        print(len(list_of_bat[1]))
        os.chdir('..')
        bowl_cluster=os.listdir(f3)
        os.chdir(f3)
        for i in bowl_cluster:
               lines=open(i).readlines()
               s=[]
               for j in lines:
                      p=j.strip('\n').split(',')
                      if len(p) >12:
                        s.append(p[13])
               if s:
                 list_of_bowl.append(s)
        print(list_of_bowl)
        os.chdir('..')
        print(os.getcwd())
        w=[]   #bowl_cluster_no,bat_cluster,bowl_name,bat_name,0,1,2,3,4,6,total
        i=0
        e=len(list_of_bat)
        f=len(list_of_bowl)
        i=0
        while i < f:   # no of clusters in bowl
                j=0
                t=[]
                q=len(list_of_bowl[i])    # no of bowlers in each cluster
                while j < q:
                      r=0
                      while r<e:
                               h=0
                               z=len(list_of_bat[r])
                               no_0=0
                               no_1=0
                               no_2=0
                               no_3=0
                               no_4=0
                               no_6=0
                               while h < z:
                                       
                                       ipl=os.listdir(f1)
                                       os.chdir(f1)
                                       for d in ipl:
                                                lines=open(d).readlines()
                                                for x in lines:
                                                        g=x.strip('\n').split(',')
                                                        if len(g) >5:
                                                            if g[6]==list_of_bowl[i][j] and g[4]==list_of_bat[r][h]:
                                                                if g[7]=='0':
                                                                        no_0+=1
                                                                elif g[7]=='1':
                                                                        no_1+=1
                                                                elif g[7]=='2':
                                                                        no_2+=1
                                                                elif g[7]=='3':
                                                                        no_3+=1
                                                                elif g[7]=='4':
                                                                        no_4+=1
                                                                elif g[7]=='6':
                                                                        no_6+=1
                                                            if g[6]==list_of_bowl[i][j] and g[5]==list_of_bat[r][h]:
                                                                if g[8]=='0':
                                                                        no_0+=1
                                                                elif g[8]=='1':
                                                                        no_1+=1
                                                                elif g[8]=='2':
                                                                        no_2+=1
                                                                elif g[8]=='3':
                                                                        no_3+=1
                                                                elif g[8]=='4':
                                                                        no_4+=1
                                                                elif g[8]=='6':
                                                                        no_6+=1
                       
                                                
                                       t.append([i,r,list_of_bowl[i][j],list_of_bat[r][h],no_0,no_1,no_2,no_3,no_4,no_6])
                                       os.chdir('..')
                                       h+=1
                               r+=1
                      j+=1
                w.append(t)
                i+=1 
        print(w)         
                
        
#prob('ipl','bat','bowl')
prob('test','bat','bowl')
