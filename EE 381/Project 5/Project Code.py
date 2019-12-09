import numpy as np
import math as m
import matplotlib
import matplotlib.pyplot as plt
import random


#This is used to randomly decide the next state based on a initial vector
#Largely based on nSidedDie from previous labs
def newStateIndex(stateArray):
## stateArray - A numpy array representing state transition probabilities
    
    #array length
    totalStateCount = stateArray.size
    #cumulative sum to act as edges of probability
    stateCumSum = np.cumsum(stateArray)
    stateOdds = np.append (0, stateCumSum)
    
    #generate random value
    randVal = np.random.rand()
    #check which CumSum values it falls between
    for state in range(0, totalStateCount):
        #If the next value is greater than the current random value,
        #the current index represents the correct state
        if randVal <=  stateOdds[(state + 1)]:
            return state



#Returns the next state randomly from the probility Vector argument
def stateSwitch(initProb):
## initProb - the transition probability vector of states
    
    return  newStateIndex(initProb)



#Randomly walks through a state transition matrix for a number of steps
#given an initial probability vector, logging steps
def StateStep ( firstState, array, stepCount):
## firstState - the initial Probability Vector
## array - the state transition matrix
## stepCount - the desired number of steps through the matrix

    #Define a means to track each state as it changes
    stateLog = np.zeros((stepCount,1))
    #set the loop variable to start at the passed probability vector
    stateProb = firstState

    #Up to a count (stepCount), 
    for i in range(0, stepCount):
        #get new state index from the current probabilty vector
        newProb = stateSwitch(stateProb)
        #log the new state
        stateLog[i] = newProb
        #Get the new probabilty vector from the new state index
        stateProb = array[newProb]

    #return the results
    return stateLog



#This function will loop through the state transition matrix approach
#to the desired power of P, then returns the probability vector of u
def dotLoop (u, P, exponentP):
## u - the initial probability vector, u(0)
## P - the state transition matrix to be transformed
## exponentP - the Power to which P is desired to be raised, or steps taken

    #Define the variable to be multiplyed so the loop can act continuously
    matrix = P

    #For (exponentP - 1) times, find the dot product of the most recent
    #P, and the original P
    for count in range (0, exponentP - 1):
        matrix = np.dot(matrix, P)

    #return the probability vector by getting the dot product of
    #u(0) and matrix, which is equal to P^exponentP
    return np.dot(u, matrix)



#This function will loop through the state transition matrix approach
#to the desired power of P, then returns the matrix
def dotLoopMatrix (u, P, exponentP):
## u - the initial probability vector, u(0)
## P - the state transition matrix to be transformed
## exponentP - the Power to which P is desired to be raised, or steps taken

    #Define the variable to be multiplyed so the loop can act continuously
    matrix = P

    #For (exponentP - 1) times, find the dot product of the most recent
    #P, and the original P
    for count in range (0, exponentP - 1):
        matrix = np.dot(matrix, P)

    #return matrix
    return matrix


#This Function 
def drunkenWalkNextState(initialState):
## walkArray - A numpy array representing state transition probabilities
## initialState - An array of the initial state probabilities
    
    #array length
    totalStateCount = initialState.size
    #cumulative sum
    stateCumSum = np.cumsum(initialState)
    stateOdds = np.append (0, stateCumSum)
    #generate random value
    randVal = np.random.rand()
    #check which CumSum values it falls between
    for state in range(0, totalStateCount):
        #check what the probability of this state occuring
        prob = initialState[state]
        #Skip if this state cannot occur from the current state
        if (prob == 0):
            continue
        #If the next value is greater than the current random value,
        #the current index represents the correct state
        if randVal <=  stateOdds[(state + 1)]:
            return state


def translatePos(intArg):
    if (intArg == 0):
        print("State - 1")
    if (intArg == 1):
        print("State - 2")
    if (intArg == 2):
        print("State - 3")
    if (intArg == 3):
        print("State - 0")
    if (intArg == 4):
        print("State - 4")

def translateLog(intArg):
    if (intArg == 0):
        return 1
    if (intArg == 1):
        return 2
    if (intArg == 2):
        return 3
    if (intArg == 3):
        return 0
    if (intArg == 4):
        return 4


    
###################################
### 1. Three-state Markov Chain ###
###################################


### ------------- Variables To Use ------------- ### 

weatherProbArray = np.array([  [ 0.33 , 0.33 , 0.34 ],
                               [ 0.34 , 0.16 , 0.50 ],
                               [ 0.40 , 0.20 , 0.40 ]])

startProb = np.array([.24999, .00001, .75])
stepCount = 15
experimentCount = 10000

### -------------------------------------------- ### 


### ------------- Run simulation ------------- ###

#Define Variables for tracking results
experimentLog = np.zeros((15,3))
rainCount = 0
niceCount = 0
snowCount = 0

#repeat the experiment up to (experimentCount) times
for index in range(0, experimentCount):

    #Walk through the transition mantrix with StateStep
    #Store the results
    experiment = StateStep(startProb, weatherProbArray, 15)
    
    
    ### Check the results, logging the occurances of each state
    ### at each given step
    index = 0
    for element in experiment:
        #If the step is a state, increase that index by 1
        if (element == 0.0):
            experimentLog[index][0] += 1
        if (element == 1.0):
            experimentLog[index][1] += 1
        if (element == 2.0):
            experimentLog[index][2] += 1
        #Move onto the next step
        index +=1

    #Log the final state of the experiment
    finalState = experiment[14][0]
    if (finalState == 0.0):
        rainCount += 1
    if (finalState == 1.0):
        niceCount += 1
    if (finalState == 2.0):
        snowCount += 1

#Divide every element of the experimentLog by the experimentCount
#To find the probability of that state occuring at that step
experimentLog = experimentLog/experimentCount

### ------------------------------------------- ###


### ------------- Display Results of Experiment ------------- ###

print ("Experimental Count of End State")
print ("Rain -" + str(rainCount))
print ("Nice -" + str(niceCount))
print ("Snow -"+ str(snowCount))
print ("Experimental Probability of  End State")
print ("Rain -" + str(rainCount/experimentCount))
print ("Nice -" + str(niceCount/experimentCount))
print ("Snow -"+ str(snowCount/experimentCount))
print (experimentLog)

### --------------------------------------------------------- ###

### ------------- Compare Results to Theoretical ------------- ###

# State Transition Matrix Approach using dotLoop
print (dotLoop(startProb, weatherProbArray, 15))

### ------------- Report Required Elements ------------- ###

### Plot one run using state step
oneRun = StateStep(startProb, weatherProbArray, 15)
    
plt.figure(1)
x1=list(range(0,15))
plt.plot(x1,oneRun,'*:', label='Current State')
plt.xticks(x1);
plt.yticks([0,1,2])
plt.title('Single Simulation of Weather Transition')
plt.xlabel('Steps Taken')
plt.ylabel('State')
plt.legend(loc='best')
plt.show()

### Plot simulated probs obtained from the earlier experiment log
Prob_A=experimentLog[:,0]
Prob_B=experimentLog[:,1]
Prob_C=experimentLog[:,2]
    
plt.figure(1)
x1=list(range(0,15))
plt.plot(x1,Prob_A,'*:', label='Rainy')
plt.plot(x1,Prob_B,'o:',label='Nice')
plt.plot(x1,Prob_C,'v:',label='Snowy')
plt.xticks(x1);
plt.title('Experimental State Transition Markov Chain')
plt.xlabel('Step Count')
plt.ylabel('Probability')
plt.legend(loc='best')
plt.show()


### Plot state transition approach
arrayPlot=weatherProbArray
initialCondition=startProb
stepNo=15 #number of steps
stateNo=3  # number of states

W=np.array([ [0.0 for i in range(0,stateNo)] for j in range(0,stepNo) ])
W[0,:]=initialCondition
    
for k in range(1,stepNo):
    W[k,:]=np.dot(W[k-1,:],arrayPlot)
    

Prob_A=W[:,0]
Prob_B=W[:,1]
Prob_C=W[:,2]
    
plt.figure(1)
x1=list(range(0,stepNo))
plt.plot(x1,Prob_A,'*:', label='Rainy')
plt.plot(x1,Prob_B,'o:',label='Nice')
plt.plot(x1,Prob_C,'v:',label='Snowy')
plt.xticks(x1);
plt.title('Calculated State Transition Markov Chain')
plt.xlabel('Step Count')
plt.ylabel('Probability')
plt.legend(loc='best')
plt.show()

### ---------------------------------------------------- ###

########################################
### 2. The Google PageRank Algorithm ###
########################################

### --------------------- Variables To Use ---------------------- ###



                            # A      B      C      D      E 
pageProbArray = np.array([  [ 0.00 , 1.00 , 0.00 , 0.00 , 0.00],  #A
                            [ 0.50 , 0.00 , 0.50 , 0.00 , 0.00],  #B
                            [ 0.33 , 0.33 , 0.00 , 0.00 , 0.33],  #C
                            [ 1.00 , 0.00 , 0.00 , 0.00 , 0.00],  #D
                            [ 0.00 , 0.33 , 0.33 , 0.33 , 0.00]]) #E

firstState = np.array([[ 0.2 , 0.2 , 0.2 , 0.2 , 0.2 ]])
secondState = np.array([[ 0 , 0 , 0 , 0 , 1 ]])

### ------------------------------------------------------------- ###

## Each version of the experiment will be walked through 20 times
repetitionCount = 20

#Perform the experiment starting from any random page
evenOddLog = []
evenOddLog.append([ 0.2 , 0.2 , 0.2 , 0.2 , 0.2 ])
for stepCount in range(0, repetitionCount):
    evenOddLog.append(dotLoop(firstState, pageProbArray, stepCount)[0])
print (evenOddLog)
eOLArray = np.array(evenOddLog)

Prob_A= eOLArray[:,0]
Prob_B= eOLArray[:,1]
Prob_C= eOLArray[:,2]
Prob_D= eOLArray[:,3]
Prob_E= eOLArray[:,4]


plt.figure(1)
x1=list(range(0,repetitionCount+1))
plt.plot(x1,Prob_A,'*:', label='Page A')
plt.plot(x1,Prob_B,'o:',label='Page B')
plt.plot(x1,Prob_C,'v:',label='Page C')
plt.plot(x1,Prob_D,'*:', label='Page D')
plt.plot(x1,Prob_E,'o:',label='Page E')
plt.xticks(x1);
plt.title('Page Rank Probability from Even Page Odds')
plt.xlabel('Step Count')
plt.ylabel('Probability')
plt.legend(loc='best')
plt.show()

#Perform the experiment starting from page E
pageELog = []
pageELog.append([ 0 , 0 , 0 , 0 , 1 ])
for stepCount in range(0, repetitionCount):
    pageELog.append(dotLoop(secondState, pageProbArray, stepCount)[0])
pELArray = np.array(pageELog)

Prob_A= pELArray[:,0]
Prob_B= pELArray[:,1]
Prob_C= pELArray[:,2]
Prob_D= pELArray[:,3]
Prob_E= pELArray[:,4]


plt.figure(1)
x1=list(range(0,repetitionCount+1))
plt.plot(x1,Prob_A,'*:', label='Page A')
plt.plot(x1,Prob_B,'o:',label='Page B')
plt.plot(x1,Prob_C,'v:',label='Page C')
plt.plot(x1,Prob_D,'*:', label='Page D')
plt.plot(x1,Prob_E,'o:',label='Page E')
plt.xticks(x1);
plt.title('Page Rank Probability Starting from Page E')
plt.xlabel('Step Count')
plt.ylabel('Probability')
plt.legend(loc='best')
plt.show()

##################################
### 3. Absorbing Markov Chains ###
##################################

### ----------- Provided Values ----------- ###

#--------------------------------------------#
# A = 2/3[0.66] B = 3/5[0.60] C = 3/10[0.30] #
#--------------------------------------------#

#----------------------------------------#
# 1-A = [0.34] 1-B = [0.40] 1-C = [0.70] #
#----------------------------------------#

### --------------------------------------- ###


### --------------------- Variables To Use ---------------------- ###


                            #|       Q          |       R     |
                            #|1      2      3   |  0      4   |       
walkProbArray = np.array([  [ 0.00 , 0.33 , 0.00 , 0.66 , 0.00],  #1
                            [ 0.60 , 0.00 , 0.40 , 0.00 , 0.00],  #2  
                            [ 0.00 , 0.30 , 0.00 , 0.00 , 0.70],  #3 ____
                            [ 0.00 , 0.00 , 0.00 , 1.00 , 0.00],  #0
                            [ 0.00 , 0.00 , 0.00 , 0.00 , 1.00]]) #4
                            #|       0          |       I     |

repetitionCount = 15
### ------------------------------------------------------------- ###


#Generate the random state from which to start the walk
randVal = 1

#Set the loop variable to the initial value determined by the randVal
stateProb = walkProbArray[randVal]

experimentLog = []
translatePos(randVal)
#Walk through the array up to 15 steps
for count in range (0,repetitionCount):
    #get new state index from the current probabilty vector
    nextIndex = drunkenWalkNextState(stateProb)
    experimentLog.append(translateLog(nextIndex))
    #Display the new state
    translatePos(nextIndex)
    #Get the new probabilty vector from the new state index
    stateProb = walkProbArray[nextIndex]

### ----------- Plot ----------- ###
eLArray = np.array(experimentLog)

plt.figure(1)
x1=list(range(0,repetitionCount))
y1= [0,1,2,3,4]
plt.plot(x1,eLArray,'*:', label='Walk State')
plt.xticks(x1)
plt.yticks(y1)
plt.title('Drunken Walk Absorbing State - Absorbed by 0')
plt.xlabel('Step Count')
plt.ylabel('State')
plt.legend(loc='best')
plt.show()
### ---------------------------- ###



##########################################################################
### 4. Compute the probability of absorption using the simulated chain ###
##########################################################################


### --------------------- Variables To Use ---------------------- ###

initialProbState = np.array ([[ 0.00 , 0.00 , 1.00 , 0.00 , 0.00 ]])

walkProbArray = np.array([  [ 0.00 , 0.34 , 0.00 , 0.66 , 0.00],  #1
                            [ 0.60 , 0.00 , 0.40 , 0.00 , 0.00],  #2  
                            [ 0.00 , 0.30 , 0.00 , 0.00 , 0.70],  #3 ____
                            [ 0.00 , 0.00 , 0.00 , 1.00 , 0.00],  #0
                            [ 0.00 , 0.00 , 0.00 , 0.00 , 1.00]]) #4
                            #|       0          |       I     |

experimentCount = 10000

### ------------------------------------------------------------- ###

### --------------- Perform Simulation --------------- ###

# use the provided initial state
firstState = initialProbState[0]
# create a means to track the experiment
experimentLog = 0

#Perform the experiment up to (experimentCount) times
for trial in range(0, experimentCount):
    #Set the loop variable's first value to the initial probability provided
    stateProb = firstState

    #This will be repeated until the end condition is found
    while (True):
        # Get the next state's index
        nextIndex = drunkenWalkNextState(stateProb)
        # using the new index, get the next state
        stateProb = walkProbArray[nextIndex]

        #Check the end condition - If the state has been absorbed by
        #either state 0 (index 3) or state 4 (index 4)
        if (nextIndex == 3 or nextIndex == 4):
            if (nextIndex == 3):
                #By logging only being absorbed by state 0, we know all 
                #other experiments ended being absorbed by state 4
                experimentLog += 1
            break
    
absorbedByZeroProb = experimentLog/experimentCount
absorbedByFourProb = (experimentCount - experimentLog)/experimentCount

print (absorbedByZeroProb)
print (absorbedByFourProb)
### -------------------------------------------------- ###






