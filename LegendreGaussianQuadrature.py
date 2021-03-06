import math
from math import *
def sub_division(f,a,b,tol,entire,results):
    #tol: user-defined tolerance
    #total: the integral on the whole interval a,b using above gaussian function
    #this function splits an integral into the right and left half and compares it to the integral on the whole function
    #if tolerance is not satisfied, the function splits the left and right into smaller intervals and repeats the function
    #when integral interval values satisfy the tolerance, they are added to the sum
    a_z=a+(b-a)/2.  #sub-divides intervals
    b_k=a+(b-a)/2.
    entire=gaussian(f,a,b)
    right=gaussian(f,a_z,b)
    left=gaussian(f,a,b_k)
    if abs(entire-(left+right))<tol * max(abs(entire), (abs(left)+abs(right))):
        results.append(entire)
        return entire
    x=sub_division(f,a_z,b,tol,right,results)+sub_division(f,a,b_k,tol,left,results)
    results.append(x)
    return x

def gaussian(f,a,b):
    #f: function that needs to be integrated
    #a,b: bounds of the integral (a<b)
    #this function is just the normal gaussian quadrature calculation with known weights
    #also uses an interval transformation so instead of just the standard interval of -1 to 1, you can use any interval
    u=(b-a)/2.*(5./9*f((b-a)/2.*-1.*sqrt(3./5)+(b+a)/2.)+8./9*f((b+a)/2.)+5./9*f((b-a)/2.*sqrt(3./5)+(b+a)/2.))
    return u

def adaptive_gaussian_quadrature(f,a,b,tol,results):
    #returns the approximate integral of f from a to b with an upper bound on the error given by the tolerance
    return sub_division(f,a,b,tol,gaussian(f,a,b),results)



#TODO:
    #To call the Gaussian Quadrature function enter the following parameters:
    #function, starting poing, ending point and tolerance.
    #The points are the limits of the integral and the tolerance will decide when to stop calculating
    #The function is defined as lambda funtion (view f below).

def main():
    f = lambda x: math.e**(3*x)  # define a function here
    results = []
    res=adaptive_gaussian_quadrature(f,-1,1, 10 ** (-5),results)
    for i in range(len(results)):
        #print(f'-Result number {i}:\nLeft:{results[i][0]}, Entire:{results[i][1]}, Right:{results[i][2]}\n')
        print(f'-Result number {i+1} : {results[i]}')
    print('\nIntegral value is', res) #input intervals and tolerance here
main()