import numpy as np 
c = np.array([2,3,4,5])             #creates an array
print(c)
print(c.dtype)
a = np.arange(2,20,2,int)           #creates an array (start,stop,step,dattyp)
print(a)
b = np.arange(15).reshape(3,5)      #creates an array with 3 rowns and 5 columns
print(b)
print(b.shape)                      #returns the shape of the array
print(b.ndim)                       #returns the axes i.e. dimension of the array
print(b.itemsize)                   #returns the size in bytes of each element

#use np.linalg.function(args) to use linear algebra functions
d = np.array([[1,2],[5,6]])     
print(d)    
x = np.linalg.inv(d)                #calculates inverse of matrix
print(x)
u = np.eye(2)                       #creates identity matrix I
print(u)
j = d @ d                           #matrix product
print(j)
print(np.trace(u))
print(np.trace(d))                  #returns the sum along the diagonals
k = np.linalg.solve(d,u)
print(k)
v = np.array([[3,2],[1,2]])
l = np.array([9,8])
q = np.linalg.solve(v,l)            #solves linear equations
print(q)
print(np.allclose(np.dot(v,q),l))   #returns True if matrices are element wise equal; dot product of two matrices
t = np.linalg.eig(u)                #calculates eigen values
print(t)


