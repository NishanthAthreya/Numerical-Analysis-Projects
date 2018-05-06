# Nishanth Athreya
# Numerical Analysis and Computing (CS323)
# Programming Assignment 1
import math
# Function for Stirling's Method
def stirling(n):
    return math.sqrt(2*math.pi*n)*math.pow(n / math.e, n)
# Function 1
def f1(x):
    return math.pow(math.e, x) - math.sin(x) - 2
# Function 2
def f2(x):
    return math.pow(x, 2) - 4*x + 4 - math.log(x)
# Derivative of Function 1
def f1p(x):
    return math.pow(math.e, x) + math.cos(x)
# Derivative of Function 2
def f2p(x):
    return 2*x -4 - (1/x)
# Function to programmatically find root (not used, so can be ignored)
def root(f, i):
    flag = True
    # i = 0
    j = 0
    pos = None
    while flag:
        #print(f(i))
        try:
            if f(i) > 0:
                if pos == False:
                    flag = False
                else:
                    j = i
                    pos = True
                    i = i + 0.01
            elif f(i) < 0:
                if pos == True:
                    flag = False
                else:
                    j = i
                    pos = False
                    i = i + 0.01
            else:
                i = i + 0.01
        except:
            i = i + 0.01

    return (j,i);

# Bisection Method
# f = function, a = initial a, b = initial b
def bisection(f, a, b, error):
    # r = root(f)
    # a = r[0]
    # b = r[1]
    c = (a + b) / 2
    # print(str(a) + " " + str(b) + " " + str(c) + " " + str(math.fabs(b-c) < math.pow(10, -10)))
    while math.fabs(b - c) >= error: # checking for error tolerance
        # print(str(a) + " " + str(b) + " " + str(c) + " " + str(math.fabs(b - c) < math.pow(10, -10)))
        if f(c) < 0:
            a = c
        elif f(c) >= 0:
            b = c
        c = (a + b) / 2.0

    return c

# Newton's Method
# f = function, fp = derivative of function, x = initial x (x0)
def newton(f, fp, x, error):
    # x = bisection(f, a , b)
    y = x - (f(x)/fp(x))
    while math.fabs(y - x) >= error: # checking for error tolerance
        x = y
        y = x - (f(x)/fp(x))

    return y

# Secant's Method
# f = function, x0 = initial x0, x1 = initial x1, x2 = initial x2
def secant(f, x0, x1, error):
    # x = root(f)
    # x0 = x[0]
    # x1 = x[1]
    x2 = x1 - f(x1)*((x1 - x0) / (f(x1) - f(x0)))
    while math.fabs(x2 - x1) >= error: # checking for error tolerance
        x0 = x1
        x1 = x2
        x2 = x1 - ((f(x1) * ((x1 - x0)) / (f(x1) - f(x0))))

    return x2


def main():
    print("Stirling's Method:")
    for n in range(1,11):
        print(str(n) + ":" + str(math.fabs(math.factorial(n) - stirling(n))) + "(Absolue), " + str(math.fabs(math.factorial(n) - stirling(n))/math.factorial(n)) + "(Relative)")
    #print(str(root(f1)[0]) + " " + str(root(f2)[1]))
    while True:
        c = input("Choose method:\n1)Bisection Method\n2)Newton's Method\n3)Secant's Method\nq)quit\n")
        if c == 'q':
            break
        if c == '1':
            print("Bisection Method (f1):")
            error = input("Enter error value(base exponent): ").split()# example input: 10 -10
            a = input("Enter a (initial): ")
            b = input("Enter b (initial): ")
            #print(bisection(f1, 0, 2, error))
            print(bisection(f1, float(a), float(b), math.pow(float(error[0]), float(error[1]))))
            print("Bisection Method (f2):")
            error = input("Enter error value(base exponent): ").split()
            a = input("Enter a (initial): ")
            b = input("Enter b (initial): ")
            #print(bisection(f2, 0.5, 3.15))
            print(bisection(f2, float(a), float(b), math.pow(float(error[0]), float(error[1]))))
        elif c == '2':
            print("Newton's Method (f1):")
            error = input("Enter error value(base exponent): ").split()
            x0 = input("Enter initial (x0): ")
            #print(newton(f1, f1p, bisection(f1, 0, 2)))
            print(newton(f1, f1p, float(x0), math.pow(float(error[0]), float(error[1]))))
            print("Newton's Method (f2): ")
            error = input("Enter error value(base exponent): ").split()
            x0 = input("Enter initial (x0): ")
            print(newton(f2, f2p, float(x0), math.pow(float(error[0]), float(error[1]))))
        elif c == '3':
            print("Secant's Method (f1):")
            error = input("Enter error value(base exponent): ").split()
            x0 = input("Enter initial (x0): ")
            x1 = input("Enter initial (x1): ")
            #print(secant(f1, 1.02125, 1.0525))
            print(secant(f1, float(x0), float(x1), math.pow(float(error[0]), float(error[1]))))
            print("Secant's Method (f2):")
            error = input("Enter error value(base exponent): ").split()
            x0 = input("Enter initial (x0): ")
            x1 = input("Enter initial (x1): ")
            #print(secant(f2, 0.5, 3.15))
            print(secant(f2, float(x0), float(x1), math.pow(float(error[0]), float(error[1]))))
        else:
            print("You didn't pick 1, 2, or 3. Press q to quit or pick of one of these values")
    # print(root(f1, 0))
    # print(root(f2, 3))
if __name__ == "__main__":
    main()