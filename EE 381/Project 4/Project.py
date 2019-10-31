import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def UnifPDF(a,b,x):
    f=(1/abs(b-a))*np.ones(np.size(x))
    return f

def ExpfPDF(beta, x):
    f = ((1/beta)*(np.exp((-x/beta)))*np.ones(np.size(x)))
    return f

def NormfPDF(mu, sigma, x):
    f = ((np.exp(-(x-mu)**2)/(2*sigma**2))/(sigma*np.sqrt(2*np.pi)))*np.ones(np.size(x))
    return f

def gaussian(mu,sig,z):
    f=np.exp(-(z-mu)**2/(2*sig**2))/(sig*np.sqrt(2*np.pi))
    return f

def BatteryProbability (beta, years):
    firstValue = (1/beta)
    secondValue = np.exp((-firstValue) * (years))
    return firstValue*secondValue

def BatteryPDF(beta, years, x):
    
    return BatteryProbability (beta, years) * np.ones(np.size(x))
    


def CLTstdDev(sigmaSum, n):
    return (sigmaSum / np.sqrt(n))

"""
###########################################################################
### 1. Simulate continuous random variables with selected distributions ###
###########################################################################

#################################################################
##### Part 1.1 - Uniform Random Variable (a = 2.0, b = 5.0) #####
#################################################################

# Generate the values of the RV X
a=2.0
b=5.0
n=10000
x=np.random.uniform(a,b,n) 

# Create bins and histogram
nbins=30 # Number of bins
edgecolor='w' # Color separating bars in the bargraph
bins=[float(x) for x in np.linspace(a, b,nbins+1)]
h1, bin_edges = np.histogram(x,bins,density=True)

# Define points on the horizontal axis
be1=bin_edges[0:np.size(bin_edges)-1]
be2=bin_edges[1:np.size(bin_edges)]
b1=(be1+be2)/2
barwidth=b1[1]-b1[0] # Width of bars in the bargraph
plt.close('all')

# PLOT THE BAR GRAPH
fig1=plt.figure(1)
plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor)

#PLOT THE UNIFORM PDF
f=UnifPDF(a,b,b1)

plt.plot(b1,f,'r')
plt.title('Uniform Random Variable: PDF - Experiment Results',fontsize=14,fontweight='bold')
plt.xlabel('Number of successes in n=1000 trials',fontsize=14)
plt.ylabel('Probability',fontsize=14)
plt.show()

#CALCULATE THE MEAN AND STANDARD DEVIATION
mu_x = np.mean(x)
sig_x = np.std(x)

Thrtcl_mu_x = (a + b)/ 2
Thrtcl_sig_x = np.sqrt((b - a) ** 2 / 12)

print ("Uniform")
print ("Mean: " + str(mu_x) + "\nStandard deviation: " + str(sig_x))
print ("T. Mean: " + str(Thrtcl_mu_x) + "\nT. Standard deviation: " + str(Thrtcl_sig_x))

##############################################################################
##### Part 1.2 - Exponentially distributed Random Variable (beta = 0.33) #####
##############################################################################

# Generate the values of the RV X
beta = 0.33
n=10000
y=np.random.exponential(beta, n)

# Create bins and histogram
nbins=2 # Number of bins
edgecolor='w' # Color separating bars in the bargraph
bins=[float(y) for y in np.linspace(0,nbins+1)]
h1, bin_edges = np.histogram(y,bins,density=True)

# Define points on the horizontal axis
be1=bin_edges[0:np.size(bin_edges)-1]
be2=bin_edges[1:np.size(bin_edges)]
b1=(be1+be2)/2
barwidth=b1[1]-b1[0] # Width of bars in the bargraph
plt.close('all')

# PLOT THE BAR GRAPH
fig1=plt.figure(1)
plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor)

#PLOT THE UNIFORM PDF
f=ExpfPDF(beta, b1)

plt.plot(b1,f,'r')
plt.title('Exponential Distributed Random Variable: PDF - Experiment Results',fontsize=14,fontweight='bold')
plt.xlabel('Number of successes in n=1000 trials',fontsize=14)
plt.ylabel('Probability',fontsize=14)
plt.show()

#CALCULATE THE MEAN AND STANDARD DEVIATION
mu_y=np.mean(y)
sig_y=np.std(y)
print ("Exponential")
print ("Mean: " + str(mu_y) + "\nStandard deviation: " + str(sig_y))

##################################################################
### Part 1.3 - Normal Random Variable (mu = 2.5, sigma = 0.75) ###
##################################################################

# Generate the values of the RV X
mu = 2.5
sigma = 0.75
n=10000
z=np.random.normal(mu,sigma,n)

# Create bins and histogram
nbins=5 # Number of bins
edgecolor='w' # Color separating bars in the bargraph
bins=[float(z) for z in np.linspace(0, nbins+1)]
h1, bin_edges = np.histogram(z,bins,density=True)

# Define points on the horizontal axis
be1=bin_edges[0:np.size(bin_edges)-1]
be2=bin_edges[1:np.size(bin_edges)]
b1=(be1+be2)/2
barwidth=b1[1]-b1[0] # Width of bars in the bargraph
plt.close('all')

# PLOT THE BAR GRAPH
fig1=plt.figure(1)
plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor)

#PLOT THE UNIFORM PDF
f=NormfPDF(mu,sigma,b1)

plt.plot(b1,f,'r')
plt.title('Normal Distributed Random Variable: PDF - Experiment Results',fontsize=14,fontweight='bold')
plt.xlabel('Number of successes in n=1000 trials',fontsize=14)
plt.ylabel('Probability',fontsize=14)
plt.show()

#CALCULATE THE MEAN AND STANDARD DEVIATION
mu_z=np.mean(z)
sig_z=np.std(z)
print ("Normal")
print ("Mean: " + str(mu_z) + "\nStandard deviation: " + str(sig_z))


#############################################################
### 2. The Central Limit Theorem (a = 2.0 cm, b = 5.0 cm) ###
#############################################################

N=100000
nbooks= 15

a= 2.0
b= 5.0

mu_x=(a+b)/2
sig_x= np.sqrt((b-a)**2/12)

X=np.zeros((N,1))

for index in range(0,N):
    booksW = np.random.uniform(a,b,nbooks)
    stackSum= np.sum(booksW)
    X[index]= stackSum

# Create bins and histogram
nbins=30 # Number of bins
edgecolor='w' # Color separating bars in the bargraph
bins=[float(x) for x in np.linspace(nbooks*a, nbooks*b,nbins+1)]
h1, bin_edges = np.histogram(X,bins,density=True)

# Define points on the horizontal axis
be1=bin_edges[0:np.size(bin_edges)-1]
be2=bin_edges[1:np.size(bin_edges)]
b1=(be1+be2)/2
barwidth=b1[1]-b1[0] # Width of bars in the bargraph
plt.close('all')

# PLOT THE BAR GRAPH
fig1=plt.figure(1)
plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor)
plt.title('Central Limit Theorom: PDF - Experiment Results',fontsize=14,fontweight='bold')
plt.xlabel('Stack width in n = ' + str(nbooks) +  ' books',fontsize=14)
plt.ylabel('Probability',fontsize=14)

#PLOT THE GAUSSIAN FUNCTION
f=gaussian(mu_x*nbooks,sig_x*np.sqrt(nbooks),b1)
plt.plot(b1,f,'r')
plt.show()
"""

################################################################################
### 3. Distribution of the Sum of Exponential RVs                            ###
###   (beta = 50 days, n = 30 batteries, Y1 = 3 yrs, Y2 = 2 yrs, Y3 = 4 yrs) ###
################################################################################

beta = 50
n = 30
repeatCount = 10000
Y1 = 3
Y2 = 2
Y3 = 4
mu = beta
sigma = beta
batteryLog = np.zeros((repeatCount, 1))

for index in range (0,repeatCount):
    
    carton = np.random.exponential(beta, n)
    batteryLog[index] = (sum(carton)/365)

# Create bins and histogram
nbins=30 # Number of bins
edgecolor='w' # Color separating bars in the bargraph
bins=[float(a) for a in np.linspace(0, nbins+1)]
h1, bin_edges = np.histogram(batteryLog,bins,density=True)

# Define points on the horizontal axis
be1=bin_edges[0:np.size(bin_edges)-1]
be2=bin_edges[1:np.size(bin_edges)]
b1=(be1+be2)/2
barwidth=b1[1]-b1[0] # Width of bars in the bargraph
plt.close('all')

# PLOT THE BAR GRAPH
fig1=plt.figure(1)
plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor)
plt.title('Central Limit Theorom: PDF - Experiment Results',fontsize=14,fontweight='bold')
#plt.xlabel('Stack width in n = ' + str(nbooks) +  ' books',fontsize=14)
plt.ylabel('Probability',fontsize=14)

#PLOT THE GAUSSIAN FUNCTION
f=BatteryPDF(beta, n, batteryLog)
plt.plot(b1,f,'r')
plt.show()


