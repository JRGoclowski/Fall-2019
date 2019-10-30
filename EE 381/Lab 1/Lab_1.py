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

def twoD6Rolls(repeatCount):

    logArray = np.zeros((repeatCount, 1))
    for index in range (0, repeatCount):
        rollArray = np.zeros((2,1))
        totalRoll = 0
        numberOfRolls = 0
        while (totalRoll != 7):
            for roll in range (0,2):
                rollArray[roll] = np.random.randint(1,7)
            numberOfRolls +=1
            totalRoll = sum(rollArray)
        logArray[index] = numberOfRolls

    return logArray

def toss100Coins():
    coin = np.random.randint(0,2,100);
    heads = sum(coin)
    if heads == 50:
        return 1
    else:
        return 0

def guessPassword(passCount, repeatCount, hackListLen):
    successCount = 0
    for index in range(0, repeatCount):
        password = np.random.randint(0, passCount)
        hackList = np.random.randint(0, passCount, hackListLen)
        if password in hackList:
            successCount += 1
    prob = successCount/repeatCount
    return prob



## Problem 1: nSided unfair die

lCount = 10000
dataArray = np.zeros((lCount, 1))
lSides = 5
probArray = np.array([0.10,  0.15,  0.20,  0.35, 0.20])
lCumSum = np.cumsum(probArray)
lOdds = np.append(0,lCumSum)

for index in range (0, lCount):
    roll = nSidedDie(probArray)
    dataArray[index] = roll

binIndex =range(1, lSides+2)
sizeOfBins=np.size(binIndex)
histogram1, bin_edges=np.histogram(dataArray, bins=binIndex)
b1=bin_edges[0:sizeOfBins - 1]
plt.close('all')
prob=histogram1/lCount
#
# Plots and labels
plt.stem(b1,prob)
plt.title('PMF for an unfair 3-sided die',fontsize=14,fontweight='bold')
plt.xlabel('Number on the face of the die',fontsize=14)
plt.ylabel('Probability',fontsize=14)
plt.xticks(b1)
plt.show()

## Problem 2: Number of rolls for a "7"
lCount = 100000
dataArray = twoD6Rolls(lCount)
binIndex =range(1, 30)
sizeOfBins=np.size(binIndex)
histogram1, bin_edges=np.histogram(dataArray, bins=binIndex)
b1=bin_edges[0:sizeOfBins - 1]
plt.close('all')
prob=histogram1/lCount
#
# Plots and labels
plt.stem(b1,prob)
plt.title('PMF for sum of two dice is "7"',fontsize=14,fontweight='bold')
plt.xlabel('Number of rolls',fontsize=14)
plt.ylabel('Probability',fontsize=14)
plt.xticks(b1)
plt.show()

## Problem 3: Getting exactly 50 heads from 100 tosses
countOfSuccess = 0
for count in range(0,100000):
    
    countOfSuccess += toss100Coins()

print (countOfSuccess/100000)

## Problem 4: Password Hacking
n = 26 ** 4
N = 1000
m = 70000
k = 7
testValue = 317800
probMWords = guessPassword(n, N, m)
probKMWords = guessPassword(n, N, k*m)
halfSuccessRate = guessPassword(n, N, testValue)
print (probMWords)
print (probKMWords)
print (halfSuccessRate)
