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
        bottomBracket = nOdds[side]
        bracketIndex = 1
        while (bottomBracket == nOdds[bracketIndex]):
            bracketIndex += 1
        if randVal > nOdds[side] and randVal <= nOdds[(side + 1)]:
            return (side)

def stateSwitchTest(P):

    possValArray = np.zeros([1,1])
    for value in range (0, P.size-1):
        print(P[value])
statsTest = np.array([[ 0.00 , 0.20 , 0.00 , 0.30, 0.00 , 0.00 , 0.50]])
print(stateSwitchTest(statsTest))
"""
    nSides = P.size
    nCumSum = np.cumsum(P)
    nOdds = np.append (0, nCumSum)
    print ("Odds = " + str(nOdds))
    randVal = np.random.rand()
    print ("random value = " + str (randVal))
    for side in range(0, nSides):
        
        bottomBracket = nOdds[side]
        #print ("BB = " + str(bottomBracket))
        bracketIndex = side
        while (nOdds[bracketIndex] == bottomBracket or nOdds[bracketIndex] < bottomBracket):
            #print ("BI = " + str (bracketIndex))
            #print ("TB would be = " + str(nOdds[bracketIndex]))
            bracketIndex += 1
        topBracket = nOdds[bracketIndex]
        #print ("TB = " + str(topBracket))
        print ("Side = " + str(side))
        print ("[ " + str (bottomBracket) + " , " + str (topBracket) + " ]")
        if randVal > bottomBracket and randVal <= topBracket:
            print ("FOUND IT")
            return (side)
    """    
def intToWeather (int):
    if (int == 0):
        return "Rain"
    if (int == 1):
        return "Nice"
    if (int == 2):
        return "Snow"
 
def StateStep ( firstState, array, stepCount):
    stateLog = np.zeros((stepCount,1))
    stateProb = np.array(firstState)
    for i in range(0, stepCount):
        newProb = stateSwitch(stateProb)
        stateLog[i] = newProb
        print (intToWeather(newProb))
        stateProb = array[newProb]
    return stateLog



"""   
stepCount = 15
experimentCount = 10000


weatherProbArray = np.array([  [ 0.33 , 0.33 , 0.33 ],
                               [ 0.33 , 0.16 , 0.50 ],
                               [ 0.40 , 0.20 , 0.40 ]])



weatherProbArray = np.array([   [ 0.50 , 0.25 , 0.25 ],
                                [ 0.50 , 0.00 , 0.50 ],
                                [ 0.25 , 0.25 , 0.50 ]])


print(StateStep(1, weatherProbArray,15))


########################################
### 2. The Google PageRank Algorithm ###
########################################
                        # A      B      C      D      E 
pageProbArray = np.array([  [ 0.00 , 1.00 , 0.00 , 0.00 , 0.00],  #A
                            [ 0.50 , 0.00 , 0.50 , 0.00 , 0.00],  #B
                            [ 0.33 , 0.33 , 0.00 , 0.00 , 0.33],  #C
                            [ 1.00 , 0.00 , 0.00 , 0.00 , 0.00],  #D
                            [ 0.00 , 0.33 , 0.33 , 0.33 , 0.00]])   #E



##################################
### 3. Absorbing Markov Chains ###
##################################

#--------------------------------------------#
# A = 2/3[0.66] B = 3/5[0.60] C = 3/10[0.30] #
#--------------------------------------------#

#----------------------------------------#
# 1-A = [0.34] 1-B = [0.40] 1-C = [0.70] #
#----------------------------------------#

                            #|       Q          |       R     |
                            # 1      2      3      0      4          
walkProbArray = np.array([  [ 0.00 , 0.34 , 0.00 , 0.66 , 0.00],  #1
                            [ 0.60 , 0.00 , 0.40 , 0.00 , 0.00],  #2  
                            [ 0.00 , 0.30 , 0.00 , 0.00 , 0.70],  #3 ____
                            [ 0.00 , 0.00 , 0.00 , 1.00 , 0.00],  #0
                            [ 0.00 , 0.00 , 0.00 , 0.00 , 1.00]]) #4
                            #|       0          |       I     |

##########################################################################
### 4. Compute the probability of absorption using the simulated chain ###
##########################################################################

initialProbState = np.array ([[ 0.00 , 0.00 , 1.00 , 0.00 , 0.00 ]])



"""








\




  
