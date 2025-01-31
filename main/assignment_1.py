'''
Ivan Schneider
1/31/2025
Programming Assignment 1 
'''
import math

def RootOfTwo():
    guess = 1.5
    diff = 1.5
    tol = 0.000001
    i = 0
    print("\t", i, " : ", guess)
    while (diff >= tol):
        i += 1
        y = guess
        guess = ((guess / 2) + (1 / guess))
        print("\t", i, " : ", guess)
        diff = abs(guess - y)
    print("\tconverges within 10^-6 after ", i, " iterations")

def BisecMethod():
    def f(x):
        return (x*x*x+4*x*x-10)
    i = 100
    count = 0
    a = -4
    b = 7
    while((i>0) and ((abs(a-b))>=0.0001)):
        count+=1
        c = (a+b)/2
        if((f(c)*f(a))<0):
            b = c
        else:
            a = c
        print("\t %.5f" %(c), "error is %.6f" %(abs(a-b)))
    
    print("\t itterations needed: ", count)

def FixedPoint(a):
    
    def ga(x):
        return (x - x*x*x - 4*x*x + 10)
    
    def gb(x):
        return (((10-x**3)**0.5)/2)
    
    guess = 1.5
    tol = 0.000001
    N = 50
    i = 0
    x = 0;
    print(i, " : ", guess)
    
    while(i<=N):
        if(a == 0):
            x = ga(guess)
        else:
            x = gb(guess)
        if(guess != guess):
            print("\tFailure, divergence after ", (i), " iterations")
            break
        print("\t", i, " : ", guess)
        if(abs(x-guess)<tol):
            N = 0
            print("\tSuccess after ", i, " iterations.")
            break
        i += 1
        guess = x

    if(N != 0 and i == 50):
        print("\tFailed to achieve precision after 50 itterations")

def NewtonRaphson():
    def f(x):
        return (math.cos(x)-x)
    def df(x):
        return (-math.sin(x)-1)
        
    guess = math.pi/4
    i=0
    print("\t", i, " : %.10f" %guess)
    while(i<4):
        i+=1
        x = guess - f(guess)/df(guess) 
        print("\t", i, " : %.10f" %x)
        guess = x
        


print("Approximation Algorithm of root of 2 to 10^-6 with a starting guess of 1.5:")
RootOfTwo()

print("\n\nBisection Method of finding the zeros of x^3 + 4x^2 - 10 to 10^-4 with starting edge values of -4 and 7:")
BisecMethod()

print("\n\nFixed Point method of finding the zeros of x^3 + 4x^2 - 10 to 10^-6 Using the fixed point formula g(x) = x - x^3 - 4*x^2 +10 with a guess value of 1.5:")
FixedPoint(0)

print("\n\nFixed Point method of finding the zeros of x^3 + 4x^2 - 10 to 10^-6 Using the fixed point formula g(x) = ((10-x^3)^0.5)/2 with a guess value of 1.5:")
FixedPoint(1)

print("\n\nNewton Raphson method of finding the zeros of cos(x)-x with 4 steps with a starting guess of pi/4:")
NewtonRaphson()

