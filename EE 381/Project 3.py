import numpy as np
import matplotlib.pyplot as plt
import math

def nSidedDie(P):
    nSides = P.size
    nCumSum = np.cumsum(P)
    nOdds = np.append (0, nCumSum)
    randVal = np.random.rand()
    for side in range(0, nSides):
        if randVal > nOdds[side] and randVal <= nOdds[(side + 1)]:
            return (side + 1)
probabilityDistribution = np.array([0.1, 0.1, 0.1, 0.3, 0.2, 0.2])
pD = probabilityDistribution


### 1. Experimental Bernoulli Trials
rollLimit = 1000
trialLimit = 10000

threeRollLog = np.zeros((3,1))
tRL = threeRollLog

successCountLog = np.zeros((trialLimit, 1))
sCL = successCountLog
for trialCount in range (trialLimit):
    print(trialCount)
    successCount = 0
    for rollTrialCount in range(0,rollLimit):
        for rollCount in range (0,3):
            tRL[rollCount] = nSidedDie(pD)
        if tRL[0] == 1:
            if tRL[1] == 2:  
                if tRL[2] == 3:
                    successCount += 1
    sCL[trialCount] = successCount

binIndex =range(0, 20)
sizeOfBins=np.size(binIndex)
histogram1, bin_edges=np.histogram(sCL, bins=binIndex)
b1=bin_edges[0:sizeOfBins - 1]
plt.close('all')
prob=histogram1/trialLimit
# Plots and labels
plt.stem(b1,prob)
plt.title('Bernouli Trials: PMF - Experiment Results',fontsize=14,fontweight='bold')
plt.xlabel('Number of successes in n=1000 trials',fontsize=14)
plt.ylabel('Probability',fontsize=14)
plt.xticks(b1)
plt.show()


### 2. Calculations using the binomial distribution
rollLimit =  1000
trialLimit = 10000
threeRollLog = np.zeros((3,1))
tRL = threeRollLog

SuccessRate = .001
FailureRate = 1 - SuccessRate
p = SuccessRate
q = FailureRate

successCountLog = np.zeros((trialLimit, 1))
sCL = successCountLog

fact = math.factorial
pwr = math.pow

for trialCount in range(0, trialLimit):
    print(trialCount)
    successCount = 0
    for testIndex in range (0, rollLimit):
        for rollIndex in range(0,3):
            tRL[rollIndex] = nSidedDie(pD)
        if tRL[0] == 1:
            if tRL[1] == 2:  
                if tRL[2] == 3:
                    successCount += 1
    #                       ((1000)!/(successes)!)/(1000 - succ))                             
    sCL[trialCount] = (fact(rollLimit) // fact(successCount) // fact(rollLimit - successCount))*(pwr(p,successCount))*(pwr(q, rollLimit - successCount))
    #               * p^successCount[k]   * q^n-successCount[k]
                    
                      
xAxis = []
for xPoint in range (0,18):
    xAxis.append(xPoint)

yAxis = []
yValues = np.flip(np.unique(sCL))
for yPoint in range(yValues.size):
    yAxis.append(yValues[yPoint])

yLen = len(yAxis)
for fillValues in range (18 - yLen):
    yAxis.append(0)
 
# Plots and labels
plt.stem(xAxis,yAxis)
plt.title('Bernouli Trials: PMF - Binomial Formula',fontsize=14,fontweight='bold')
plt.xlabel('Number of successes in n=1000 trials',fontsize=14)
plt.ylabel('Probability',fontsize=14)
plt.xticks(np.arange(0,18,1))
plt.show()


### 3. Approximation of Binomial by Poisson Distribution
rollLimit =  1000
trialLimit = 10000
threeRollLog = np.zeros((3,1))
tRL = threeRollLog

SuccessRate = .001
FailureRate = 1 - SuccessRate
p = SuccessRate
q = FailureRate

successCountLog = np.zeros((trialLimit, 1))
sCL = successCountLog

fact = math.factorial
pwr = math.pow
exp = math.exp

for trialCount in range(0, trialLimit):
    print(trialCount)
    successCount = 0
    for testIndex in range (0, rollLimit):
        for rollIndex in range(0,3):
            tRL[rollIndex] = nSidedDie(pD)
        if tRL[0] == 1:
            if tRL[1] == 2:  
                if tRL[2] == 3:
                    successCount +=1
    lamda = rollLimit * p
    sCL[trialCount] = ((pwr(lamda, successCount)) * (exp(-(lamda))))/ fact(successCount)

xAxis = []
for xPoint in range (0,18):
    xAxis.append(xPoint)

yAxis = []
yValues = np.flip(np.unique(sCL))
for yPoint in range(yValues.size):
    yAxis.append(yValues[yPoint])

yLen = len(yAxis)
for fillValues in range (18 - yLen):
    yAxis.append(0)
 
# Plots and labels
plt.stem(xAxis,yAxis)
plt.title('Bernouli Trials: PMF - Poisson Approximation',fontsize=14,fontweight='bold')
plt.xlabel('Number of successes in n=1000 trials',fontsize=14)
plt.ylabel('Probability',fontsize=14)
plt.xticks(np.arange(0,18,1))
plt.show()



