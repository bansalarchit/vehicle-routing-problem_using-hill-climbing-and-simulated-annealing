from random import shuffle
import random
from matplotlib import pyplot as plt
import time
import math

def distance(x1,x2,y1,y2):
    return ((x1-x2)**2 +(y1-y2)**2)**0.5

def matrix_formation (xcor,ycor):
    matrix=[]
    for i in range(len(xcor)):
        row=[]
        for j in range(len(xcor)):
            row.append(distance(xcor[i],xcor[j],ycor[i],ycor[j]))
        matrix.append(row)

    return matrix
    
def objectfunct (row):
    value=0
    i=0
    for items in row:
        if items!=row[cities-1]:
            value+=matrix[row[i]][row[i+1]]
        else:
            value+=matrix[row[i]][row[0]]
        i=i+1
    return value
    
def swap(co,inx1,inx2):
    p=co[inx1]
    co[inx1]=co[inx2]
    co[inx2]=p
    return co

def neighbour (state):
    neighbors=[]
    
    for i in range(1,cities):
        for j in range(i+1,cities):
            ans=swap(state.copy(),i,j)
            neighbors.append(ans)
    return neighbors
def probablity(curr_cost,next_cost):
    if curr_cost>next_cost:
        return 1
    else:
        return math.exp(-abs(next_cost-curr_cost)/temp)

    
def simulatedannealing(state):
    curr=objectfunct(state)
    neighbourlist = neighbour(state)
    for items in neighbourlist:
        p=probablity(objectfunct(state),objectfunct(items))
        #print("p",p)
        rand_num=random.random()
        
        if rand_num < p:
            #print("p",p)
            #print("r",rand_num)
            #print("yes it works")
            state=items

    solution=[objectfunct(state),state]
    return solution

def hillclimbing_r_restart(state):
    curr=objectfunct(state)
    #print(curr)
    neighbourlist=neighbour(state)
    for items in neighbourlist:
        #print(items)
        if objectfunct(items) < objectfunct(state):
            #print("y",items)
            #print(objectfunct(items))
            state=items
        #else:
            #print("n",items)
            #print(objectfunct(items))
            

    solution=[objectfunct(state),state]
    return solution

def hillclimbing_r_walk(state):
    curr=objectfunct(state)
    #print(curr)
    neighbourlist=neighbour(state)
    for items in neighbourlist:
        #print(items)
        if objectfunct(items) < objectfunct(state):
            if random.random()<0.85:
                state=items
        else:
            if random.random()<0.15:
                state=items
            
            

    solution=[objectfunct(state),state]
    return solution
"""
def plot_route(path):
    x_update=[]
    y_update=[]
    for k,city in enumerate(path):
        t=city
        x_update.append(xcor[t])
        y_update.append(ycor[t])

    x_update.append(xcor[path[0] ])
    y_update.append(ycor[path[0] ])
    plt.plot(x_update,y_update)
    plt.scatter(x_update,y_update,label='cities',color='k')
    for i in range (len(xcor)):
        plt.text(xcor[i]+90 , ycor[i]+90 , str(i), fontsize=9)
    plt.title("distance travelled ="+ str(objectfunct(path)))
    plt.show(block=False)
    plt.pause(0.2)
    plt.close()
"""
    
    
    
if __name__ == "__main__":
     algo= input("Which Algorithm you would like to run on problem : Enter 1 for hill climbing with random restart or Enter 2 for hill climbing with random walk and enter 3 for simulated annealing or enter any value >3 to terminate the program\n")
     while int(algo) < 4:
         if int(algo) == 1 :
             xcor= [0]      # list to store x co-ordinates
             ycor= [0]       # list to store y co-ordinates
             data=input("To evaluate 9 customer's data set enter 1 or To evaluate 48 customer data set enter 2\n")

             if int(data)==1:
                 with open(r".\15citydataset.txt","r") as f:                 # reading of text file that includes coordinates of the cities
                     for line in f:
                         x, y = line.split()
                         xcor.append(int(x))
                         ycor.append(int(y))
                         
             elif int(data)==2:
                 with open(r".\vrpdataset.txt","r") as f:                 # reading of text file that includes coordinates of the cities
                      for line in f:
                          x, y = line.split()
                          xcor.append(int(x))
                          ycor.append(int(y))
             else:
                 break
            
                         
             matrix=matrix_formation(xcor,ycor)

             cities=len(xcor)                                    # number of cities
             initsol=[]
             for i in range(cities-1):
                 initsol.append(i+1)
             states=initsol                                       # starting solution
            #print(objectfunct(state))
             m=100                                                # number of times solution is given random restart
             cost=[]
             start=time.time()                                   # start time 
             while m>0:
                 
             
                 m=m-1
                 state=[0]
                 shuffle(states)                                  #random start state
                 state+=states
                 print("initial_route",state)
                 print("starting_state_cost=",objectfunct(state))    # starting state cost
                 solution=hillclimbing_r_restart(state)
                 print("path_evaluated=",solution[1])
                 #plot_route(solution[1])
                 
            
                 print("cost=",solution[0])
                 print(" ")
                 cost.append(solution)

             cost.sort()    
             end=time.time()
    
             print("runtime=",end-start)
             print("final_cost",cost[0][0])
             print("final_path",cost[0][1])
             
             x_new=[]
             y_new=[]
             for city in cost[0][1]:
                 x_new.append(xcor[city])
                 y_new.append(ycor[city])
        
             x_new.append(xcor[cost[0][1][0] ])
             y_new.append(ycor[cost[0][1][0] ])
             plt.plot(x_new,y_new)
             plt.scatter(x_new,y_new,label='cities',color='k')
        
             for i in range (len(xcor)):
            
                 plt.text(xcor[i]+90 , ycor[i]+90 , str(i), fontsize=9)
        
             plt.title("distance travelled ="+ str(objectfunct(cost[0][1])))
             plt.show()
    

         elif int(algo) == 2:
             xcor= [0]      # list to store x co-ordinates
             ycor= [0]       # list to store y co-ordinates
             data=input("To evaluate 9 customer's data set enter 1 or To evaluate 48 customer data set enter 2\n")

             if int(data)==1:
                 with open(r".\15citydataset.txt","r") as f:                 # reading of text file that includes coordinates of the cities
                     for line in f:
                         x, y = line.split()
                         xcor.append(int(x))
                         ycor.append(int(y))
                         
             elif int(data)==2:
                 with open(r".\vrpdataset.txt","r") as f:                 # reading of text file that includes coordinates of the cities
                      for line in f:
                          x, y = line.split()
                          xcor.append(int(x))
                          ycor.append(int(y))
             else:
                 break

             matrix=matrix_formation(xcor,ycor)

             cities=len(xcor)                                    # number of cities
             initsol=[]
             for i in range(cities-1):
                 initsol.append(i+1)
                 states=initsol                                       # starting solution
        #print(objectfunct(state))
             m=100                                               # number of times solution is given random restart
             cost=[]
             start=time.time()                                   # start time
             u=True
             while m>0:
                 m=m-1
                 if u:
                     state=[0]
                     shuffle(states)                                  #random start state
                     state+=states
            #print("state",state)
                 print("initial_route",state)
                 print("starting_state_cost=",objectfunct(state))    # starting state cost
                 solution=hillclimbing_r_walk(state)
                 print("path_evaluated=",solution[1])
                # plot_route(solution[1])
        
                 state=solution[1]
                 u=False
                 print("cost=",solution[0])
                 print(" ")
                 cost.append(solution)
        
             cost.sort()
             end=time.time()
             #print(matrix)
             print("runtime=",end-start)
             print("final_cost",cost[0][0])
             print("final_path",cost[0][1])
             x_new=[]
             y_new=[]
        
             for city in cost[0][1]:
                 x_new.append(xcor[city])
                 y_new.append(ycor[city])
        
             x_new.append(xcor[cost[0][1][0] ])
             y_new.append(ycor[cost[0][1][0] ])
             plt.plot(x_new,y_new)
             plt.scatter(x_new,y_new,label='cities',color='k')
        
             for i in range (len(xcor)):
                 plt.text(xcor[i]+90 , ycor[i]+90 , str(i), fontsize=9)
             plt.title("distance travelled ="+ str(objectfunct(cost[0][1])))
             plt.show()

         elif int(algo)==3:
             temp =10
             alpha=0.9995
             xcor= [0]      # list to store x co-ordinates
             ycor= [0]       # list to store y co-ordinates
             data=input("To evaluate 9 customer's data set enter 1 or To evaluate 48 customer data set enter 2\n")

             if int(data)==1:
                 with open(r".\15citydataset.txt","r") as f:                 # reading of text file that includes coordinates of the cities
                     for line in f:
                         x, y = line.split()
                         xcor.append(int(x))
                         ycor.append(int(y))
                         
             elif int(data)==2:
                 with open(r".\vrpdataset.txt","r") as f:                 # reading of text file that includes coordinates of the cities
                      for line in f:
                          x, y = line.split()
                          xcor.append(int(x))
                          ycor.append(int(y))
             else:
                 break

             matrix=matrix_formation(xcor,ycor)

             cities=len(xcor)                                    # number of cities
             initsol=[]
             for i in range(cities-1):
                 initsol.append(i+1)
                 states=initsol                                       # starting solution
        #print(objectfunct(state))
             m=50                                                # number of times solution is given random restart
             cost=[]
             start=time.time()
             shuffle(states)
             state=[0]
             state+=states
             while m>0 and temp>0:
                 temp=alpha*temp
                 m=m-1
                 print("starting_state_cost=",objectfunct(state))    # starting state cost
                 solution=simulatedannealing(state)
                 print("path_evaluated=",solution[1])
                 #plot_route(solution[1])
                 print("cost=",solution[0])
                 print(" ")
                 cost.append(solution)
                 state =solution[1]
             cost.sort()
             end=time.time()
             #print(matrix)
             print("runtime=",end-start)
             print("final_cost",cost[0][0])
             print("final_path",cost[0][1])
             x_new=[]
             y_new=[]
        
             for city in cost[0][1]:
                 x_new.append(xcor[city])
                 y_new.append(ycor[city])
        
             x_new.append(xcor[cost[0][1][0] ])
             y_new.append(ycor[cost[0][1][0] ])
             plt.plot(x_new,y_new)
             plt.scatter(x_new,y_new,label='cities',color='k')
        
             for i in range (len(xcor)):
                 plt.text(xcor[i]+90 , ycor[i]+90 , str(i), fontsize=9)
             plt.title("distance travelled ="+ str(objectfunct(cost[0][1])))
             plt.show()    
         algo= input("Which Algorithm you would like to run on problem : Enter 1 for hill climbing with random restart or Enter 2 for hill climbing with random walk and enter 3 for simulated annealing or enter any value >3 to terminate the program\n")
     print("Program is terminated as either you enter value greater then 3 at first input or greater than 2 at second input")
