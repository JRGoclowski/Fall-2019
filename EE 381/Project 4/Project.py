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
    f = (np.exp(-(x-mu)**2)/(2*sigma**2))/(sigma*np.sqrt(2*np.pi)))*np.ones(np.size(x)))
    return f



## 1. Simulate continuous random variables with selected distributions

# The following code provides a way to create the bar graph of a
# uniform probability distribution in the interval [a,b)
# where  a=1, b=3.
# The code generates n=10000 values of the random variable.
# This is only a sample code. Your project has different values
# of a and b. You must use the correct values for
"""
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
f=UnifPDF(1,3,b1)

plt.plot(b1,f,'r')
plt.title('Uniform Random Variable: PDF - Experiment Results',fontsize=14,fontweight='bold')
plt.xlabel('Number of successes in n=1000 trials',fontsize=14)
plt.ylabel('Probability',fontsize=14)
plt.show()

#CALCULATE THE MEAN AND STANDARD DEVIATION
mu_x=np.mean(x)
sig_x=np.std(x)
print ("Uniform")
print ("Mean: " + str(mu_x) + "\nStandard deviation: " + str(sig_x))

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
bins=[float(y) for y in np.linspace(beta,nbins+1)]
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
f=ExpfPDF(beta,b1)

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
"""
########################################################
##### Part 1.3 - Normal Random Variable (mu = 2.5, sigma = 0.75) #####
########################################################

# Generate the values of the RV X
mu = 2.5
sigma = 0.75
n=10000
z=np.random.normal(mu,sigma,n)

# Create bins and histogram
nbins=30 # Number of bins
edgecolor='w' # Color separating bars in the bargraph
bins=[float(z) for z in np.linspace(sigma, mu, nbins+1)]
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

"""

### 2. The Central Limit Theorem

#The code provides a way to create the bar graph at the end
# for n=2 and a=1, b=3
# This is only a sample code. Your project has different values
# of a and b. You must use the correct values for your project
# Generate the values of the RV X
N=100000
nbooks=2
a=1
b=3
mu_x=(a+b)/2
sig_x=np.sqrt((b-a)**2/12)
X=np.zeros((N,1))
for k in range(0,N):
    x=np.random.uniform(a,b,nbooks)
    w=np.sum(x)
    X[k]=w
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
#PLOT THE GAUSSIAN FUNCTION
def gaussian(mu,sig,z):
    f=np.exp(-(z-mu)**2/(2*sig**2))/(sig*np.sqrt(2*np.pi))
    return f
f=gaussian(mu_x*nbooks,sig_x*np.sqrt(nbooks),b1)
plt.plot(b1,f,'r') 


### 3. Distribution of the Sum of Exponential RVs
"""
