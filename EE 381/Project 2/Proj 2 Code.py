import numpy as np
import matplotlib.pyplot as plt

def nSidedDie(P):

    nSides = P.size
    nCumSum = np.cumsum(P)
    nOdds = np.append (0, nCumSum)
    randVal = np.random.rand()
    for side in range(0, nSides):
        if randVal > nOdds[side] and randVal <= nOdds[(side + 1)]:
            return (side + 1)

probZero = 0.35
epsZero = 0.04
epsOne = 0.07
probArray = np.array([probZero, 1 - probZero])
epsZeroArray = np.array([1- epsZero, epsZero])
epsOneArray = np.array([epsOne, 1 - epsOne])

##1. Probability of Erroneous Transmission
lRepeats = 100000
lErrorCount = 0
for index in range (0,lRepeats):
    S = (nSidedDie(probArray) - 1)
    if S == 1:
        R = (nSidedDie(epsOneArray) - 1)
    else:
        R = (nSidedDie(epsZeroArray) - 1)
    if R != S:
        lErrorCount += 1
lProbError = lErrorCount / lRepeats
print (lProbError)

##2. Conditional Probability: P( R=1 | S=1 )
R = 0
lRepeats = 100000
lConditionCount = 0
lSuccessCount = 0
for index in range (0,lRepeats):
    S = (nSidedDie(probArray) - 1)
    if S == 1:
        lConditionCount += 1
        R = (nSidedDie(epsOneArray) - 1)
        if R == S:
            lSuccessCount += 1
    else:
        pass
    
lCondProb = lSuccessCount / lConditionCount
print (lCondProb)

##3. Conditional Probability: P( S=1 | R=1 )
R = 0
S = 0
lRepeats = 100000
lConditionCount = 0
lSuccessCount = 0
for index in range (0,lRepeats):
    S = (nSidedDie(probArray) - 1)
    if S == 1:
        R = (nSidedDie(epsOneArray) - 1)
        if R == 1:
            lConditionCount += 1
    else:
        R = (nSidedDie(epsZeroArray) - 1)
        if R == 1:
            lConditionCount += 1
    if S == 1 and R == 1:
        lSuccessCount += 1
    
lCondProb = lSuccessCount / lConditionCount
print (lCondProb)

## 4. Enhanced Tranmission method
lSArray = np.zeros((3,1))
lRArray = np.zeros((3,1))
D = 0

lRepeats = 100000
lSuccessCount = 0
for index in range (0,lRepeats):
    S = (nSidedDie(probArray) - 1)
    for count in range(0,3):
        if S == 1:
            lSArray[count] = 1
            lRArray[count] = (nSidedDie(epsOneArray) - 1)
        else:
            lSArray[count] = 0
            lRArray[count] = (nSidedDie(epsZeroArray) - 1)
    if sum(lSArray) > 0:
        if sum(lRArray) >= 2:
            lSuccessCount += 1

    else:
        if sum(lRArray) <= 1:
            lSuccessCount += 1
lProbSuccess = lSuccessCount / lRepeats
lProbError = 1 - (lProbSuccess)
print (lProbError)


