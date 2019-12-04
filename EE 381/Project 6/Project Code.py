import numpy 
import math as m
import matplotlib
import matplotlib.pyplot as plt

"""
P=numpy.array([ [0.75, 0.25, 0.00],
                [0.00, 0.66, 0.33],
                [0.25, 0.25, 0.50] ])
print ("P")
print (P)
Pt=numpy.transpose(P)
print ("Pt")
print (Pt)
L,W=numpy.linalg.eig(Pt)
print ("L")
print (L)
print ("W")
print (W)
k0=numpy.where(abs(L-1.0)<1e-6)
print ("k0")
print (k0)
k=k0[0][0]
print ("K")
print (k)
W=numpy.transpose(W)
print ("W")
print (W)
w=W[k,:]/sum(W[k,:])
print (w)


print ()
"""

matrix = numpy.array([  [ 0.5 , 0.5 ],
                        [ 0.125 , 0.875 ]])
a = matrix
b = numpy.matmul(a,a)
print(b)
for i in range(0,15):
    print ("n = " + str(i+3))
    b = numpy.matmul(b,a)
    print(b)
print(b)
