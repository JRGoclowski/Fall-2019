import numpy as np
import matplotlib.pyplot as plt

def MultiCoinToss(N):
    coin = np.random.randint(0,2,N);
    heads = sum(coin)
    tails = N - heads
    #
    p_heads = heads/N
    p_tails = tails/N
    print('probability of heads = ', p_heads)
    print('probability of tails = ', p_tails)

def nSidedDie(P):

    nSides = P.size
    nCumSum = np.cumsum(P)
    nOdds = np.append (0, nCumSum)
    randVal = np.random.rand()
    for side in range(0, nSides):
        if randVal > nOdds[side] and randVal <= nOdds[(side + 1)]:
            return (side + 1)

def twoD6Roll():

    rollArray = np.zeros((2,1))
    totalRoll = 0
    numberOfRolls = 0
    while (totalRoll != 7):
        print ("The roll count is " + str(numberOfRolls))
        for roll in range (0,2):
            rollArray[roll] = np.random.randint(1,7)
        numberOfRolls +=1
        totalRoll = sum(rollArray)
        print ("The roll was " + str(totalRoll))

    print ("SUCCESS!")
    return numberOfRolls
    
    
lCount = 10000
logArray = np.zeros((lCount, 1))
lSides = 5
probArray = np.array([0.10,  0.15,  0.20,  0.35, 0.20])
lCumSum = np.cumsum(probArray)
lOdds = np.append(0,lCumSum)

for index in range (0, lCount):
    roll = nSidedDie(probArray)
    logArray[index] = roll

for index in range (0, 15):
    print (twoD6Roll())

"""
b=range(1, lSides+2)
sb=np.size(b)
h1, bin_edges=np.histogram(logArray, bins=b)
b1=bin_edges[0:sb-1]
plt.close('all')
prob=h1/lCount
#
# Plots and labels
plt.stem(b1,prob)
#plt.title('PMF for an unfair 3-sided die',fontsize=14,fontweight='bold')
#plt.xlabel('Number on the face of the die',fontsize=14)
#plt.ylabel('Probability',fontsize=14)
plt.xticks(b1)
"""
