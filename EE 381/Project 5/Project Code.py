import numpy as np
import math as m
import matplotlib
import matplotlib.pyplot as plt

def XBar(data):
    return sum(data)/ np.size(data)

def SigmaXBar(sigma, n):
    return sigma/m.sqrt(n)

def sHat(data, xBar, n):
    indVar = np.zeros((n,1))
    for index in range(0, np.size(data)):
        indVar[index] = (data[index] - xBar)**2
    return ((sum(indVar)/n-1)**(0.5))

def SigmaN(data, xBar, n):
    return sHat(data,xBar,n)/m.sqrt(n)
    
def Normalize(xBar, mu, sigmaN):
    return ((xBar - mu)/sigmaN)

def CILarge(desiredInterval):
    pass
def CISmall(desiredInterval):
    pass
def muInterval(XBar, sHat, criticalValue, n):
    muInterval = np.zeros((2,1))
    muInterval[0] = XBar - (criticalValue*(sHat/m.sqrt(n)))
    muInterval[1] = XBar + (criticalValue*(sHat/m.sqrt(n)))
    return muInterval

N = 1200000
mu = 45
sigma = 3
n = 180

totalBearings = N
popMean = mu
popSTD = sigma
sampleSize = n

########################################################
### 1. Effect of sample size on confidence intervals ###
########################################################
sampData = np.zeros((n,1))
sampXbar = np.zeros((n,1))
sampSigXbar = np.zeros((n,1))
sampSize = np.zeros((n,1))
muLine = np.full((n,1), mu)

for index in range(1,n + 1):
    sampData = np.random.normal(mu, sigma, index)
    sampXbar[index - 1] = XBar(sampData)
    sampSigXbar[index - 1] = SigmaXBar(sigma, index)
    sampSize[index - 1] = index

PositiveCI95 = np.zeros((n,1))
NegativeCI95 = np.zeros((n,1))

for index in range(0,n):
    PositiveCI95[index] = mu + 1.96*(sampSigXbar[index])
    NegativeCI95[index] = mu - 1.96*(sampSigXbar[index])
    plt.plot(sampSize[index], sampXbar[index], 'b', marker = 'x')

plt.title("Sample Means and 95% confidence intervals", fontsize = 14, fontweight = 'bold')
plt.xlabel("Sample Size", fontsize = 14)
plt.ylabel("X_bar", fontsize = 14)
plt.plot(sampSize, PositiveCI95, 'r',linestyle = '--')
plt.plot(sampSize,muLine,'k')
plt.plot(sampSize, NegativeCI95,'r',linestyle = '--')
plt.show()

PositiveCI99 = np.zeros((n,1))
NegativeCI99 = np.zeros((n,1))

for index in range(0,n):
    PositiveCI99[index] = mu + 2.58*(sampSigXbar[index])
    NegativeCI99[index] = mu - 2.58*(sampSigXbar[index])
    plt.plot(sampSize[index], sampXbar[index], 'b', marker = 'x')

plt.title("Sample Means and 99% confidence intervals", fontsize = 14, fontweight = 'bold')
plt.xlabel("Sample Size", fontsize = 14)
plt.ylabel("X_bar", fontsize = 14)
plt.plot(sampSize, PositiveCI99, 'g',linestyle = '--')
plt.plot(sampSize,muLine,'k')
plt.plot(sampSize, NegativeCI99,'g',linestyle = '--')
plt.show()
    
