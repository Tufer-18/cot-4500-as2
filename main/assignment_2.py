import numpy as np


#Neville's method---------------------------------------------------------------------------------------------

#Define data points
x = np.array([...,...,...]) # X values go here.
val = np.array([...,...,...]) f(x) values go here.
w = ... # This is used to estimate a value, such as f(2.2).

#Initialize Neville array
Neville = np.zeros((len(x), len(x)))
for i in range (len(x)):
    Neville[i,0] = val[i]

#Compute the Neville's interpolation
for i in range (1,len(x)):
    for j in range(1, i+1):
        term1 = (w-x[i-j])*Neville[i,j-1]
        term2 = (w-x[i])*Neville[i-1,j-1]
        Neville[i,j] = (term1 - term2) / (x[i]-x[i-j])

#Print Neville's Interpolation
print(f"{Neville[2,2]}", end= " ") 
print("\n")



#Newton method---------------------------------------------------------------------------------------------------

def calc_div_diff(xi,fxi):
    n = len(xi)
    diffs = [[0 for j in range(n)] for i in range(n)]

    for i in range(n):
        diffs[i][0] = fxi[i]

    for i in range(1,n):
        for j in range(1, i+1):
            diffs[i][j] = (diffs[i][j-1] - diffs[i-1][j-1])/(xi[i] - xi[i-j])

    return diffs

def print_diff_table(diffs):
    n = len(diffs)
    for i in range(n):
        for j in range(i+1):
            print(f"{diffs[i][j]:+0.7f}  ", end = "")
        print()

xi = [...,...,...,...] # x values of a table go here.
fxi = [..., ..., ..., ...] # f(x) values of a table go here.

diffs = calc_div_diff(xi, fxi)


print(f"{diffs[1][1]:+0.7f}\n", end = "")
print(f"{diffs[2][2]:+0.7f}\n", end = "")
print(f"{diffs[3][3]:+0.7f}\n\n", end = "")

Newton Approx---------------------------------------------------------------------------------------------------

x = ... # Enter an x value for which you wish to approximate f(x).
approx = diffs[0][0] + diffs[1][1]*(x - x0);
print(approx) 
print("\n")


#Hermite with divided differences----------------------------------------------------------------------------

matrix = np.array([[..., ..., ..., ..., ...], [..., ..., ..., ..., ...],[..., ..., ..., ..., ...],
                   [..., ..., ..., ..., ...],[..., ..., ..., ..., ...],[..., ..., ..., ..., ...]]) #Enter your 6 by 5 matrix here.

matrix[2,2]= (matrix[2,1] - matrix[1,1])/(matrix[2,0] - matrix[1,0])
matrix[4,2]= (matrix[4,1] - matrix[3,1])/(matrix[4,0] - matrix[3,0])
matrix[2,3]= (matrix[2,2] - matrix[1,2])/(matrix[3,0] - matrix[1,0])
matrix[3,3]= (matrix[3,2] - matrix[2,2])/(matrix[3,0] - matrix[1,0])
matrix[4,3]= (matrix[4,2] - matrix[3,2])/(matrix[4,0] - matrix[2,0])
matrix[5,3]= (matrix[5,2] - matrix[4,2])/(matrix[5,0] - matrix[3,0])
matrix[3,4]= (matrix[3,3] - matrix[2,3])/(matrix[3,0] - matrix[0,0])
matrix[4,4]= (matrix[4,3] - matrix[3,3])/(matrix[4,0] - matrix[1,0])
matrix[5,4]= (matrix[5,3] - matrix[4,3])/(matrix[5,0] - matrix[2,0])
with np.printoptions(precision = 8,linewidth = 200):
    print(matrix)
print("\n")

#Cubic spline----------------------------------------------------------------------------------------------------------

h1, h2, h3 = ..., ..., ... # Enter the value of steps here.

A = np.array([[1,0,0,0],[h1, 2*(h1 + h2), h2, 0],
              [0,h2,2*(h2+h3), h3],
              [0,0,0,1]], dtype = float)

f1,f2,f3,f4 = ..., ..., ..., ... # Enter f(x) values here.

b = np.array([0,0,
              (6/h2)*(f4-f3)-(6/h3),0],dtype = float)

x = np.linalg.solve(A,b)

print(A)
print(b)
print(x) 
