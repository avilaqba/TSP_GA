import numpy as np
import random

CityList = []
lines = open(r'Distances.txt').readlines()
dc = 0
matrix = np.zeros(shape = (8,9))     
for line in lines:                   # Creating a city-list and a matrix of distances
    if line.startswith('Distance'):
        for city in range(1,9):
            CityList.append(line.split(',')[city].split('\n')[0])
    else:
        for city in range(1,9):
            matrix[dc,city] = int(line.split(',')[city])
        dc += 1
Natrix = matrix[:8,1:]

def SUM(inp):                       # A function in order to get sum of distances of every route (Fitness of every chromosome)
    S = 0
    s = 0
    for sd in d:
        S += Natrix[sd,s]
        s = sd
    return(S)
RandomList = []
N = 1000
for pop in range(N):               # Creating the first generation with a number of population of 1000.
    RandomList.append([[0]+list(np.random.choice(np.arange(1,8), 7, replace=False))+[0]])
Sum = []
for pop in range(N):
    for d in RandomList[pop]:
        Sum.append(SUM(d))     
print 'The initial distance is %d kilometers.'%Sum[0] # Printing an initial distance

Routes,Distances = [], []
for g in range(100):               # A hundred generations is considered!
    Usum = Sum + [0]
    Usum.sort()
    Fit = Usum[1:N/10]             # According to Steady-state modality, the best ten percent
    Fitlist = []                   # of the previous generation is considered for further selection.
    for FR in Fit:                 
        Fitlist.append(RandomList[Sum.index(FR)])
    Plist = []                     # Fitness of distances
    for v in range(len(Fit)+1):   
        Plist.append(sum(Fit[:v])/sum(Fit)) 
        
    RP1, RP2, P1, P2 = [], [], [], []
    for n in range(N/20):         # Selection according to roulette wheel method
        RP1.append(random.uniform(0,1))
        RP2.append(random.uniform(0,1))
    for n in range(N/20):
        for P in Plist:
            if P > RP1[n]:
                P1.append(Plist.index(P))
                break
    for n in range(len(RP2)): 
        for P in Plist:
            if P > RP2[n]:
                P2.append(Plist.index(P))
                break     
                             
    Child_1, Child_2 = [], []     # Crossover and Mutation
    for n in range(len(RP1)):
        Child_1.append([Fitlist[P1[n]-1][0][:5]])
        for r in Fitlist[P2[n]-1][0]:
            if r not in Child_1[n][0]:
                Child_1[n][0].append(r)
        Child_1[n][0].append(0)
        Child_2.append([Fitlist[P2[n]-1][0][:5]])
        for r in Fitlist[P1[n]-1][0]:
            if r not in Child_2[n][0]:
                Child_2[n][0].append(r)
        Child_2[n][0].append(0)
    RandomList = Child_1 + Child_2
    Sum = []
    for pop in range(len(RandomList)):
        for d in RandomList[pop]:
            Sum.append(SUM(d))
    Distances.append(min(Sum))
    Routes.append(RandomList[Sum.index(min(Sum))])
                                 # Priting the global minima distance and correlating route!
print 'The final distance is %d, and the route is as follows;'%min(Distances) # According to this GA algorithm, 3759km is the global minima distance!
for rt in Routes[Distances.index(min(Distances))][0]:
    print '%d.'%rt, CityList[rt]  
