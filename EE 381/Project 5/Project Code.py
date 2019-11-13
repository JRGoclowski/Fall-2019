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

sample = np.random.normal(mu, sigma, n)
print(sample)
print("Xbar: " + str(XBar(sample)))
print("Sigma Xbar: " + str(SigmaXBar(sigma, n)))
print("S hat: " + str(sHat(sample, XBar(sample), n)))
print("Sigma n: " + str(SigmaN(sample, XBar(sample), n)))
