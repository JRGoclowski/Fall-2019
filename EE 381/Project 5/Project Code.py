import numpy as np
import math as m
import matplotlib
import matplotlib.pyplot as plt


###################################
### 1. Three-state Markov Chain ###
###################################

def stateSwitch(P):

    nSides = P.size
    nCumSum = np.cumsum(P)
    nOdds = np.append (0, nCumSum)
    randVal = np.random.rand()
    for side in range(0, nSides):
        if randVal > nOdds[side] and randVal <= nOdds[(side + 1)]:
            return (side)

 
def StateStep ( firstState, array, stepCount):
    stateLog = np.zeros((stepCount,1))
    stateProb = array[firstState]
    for i in range(0, stepCount):
        newProb = stateSwitch(stateProb)
        stateLog[i] = newProb
        print (newProb)
        stateProb = array[newProb]
    return stateLog

stepCount = 15
experimentCount = 10000

StateTrans = np.array([[ 0.50 , 0.25 , 0.25 ],
                       [ 0.50 , 0.00 , 0.50 ],
                       [ 0.25 , 0.25 , 0.50 ]])

print(StateStep(1, StateTrans,15))
