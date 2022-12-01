# Created by Spencer Boggs
import math
print("")
print("       Welcome to Euler's")
print("         Method Solver!")
print("    Created by Spencer Boggs")
print("")
print("  Remember to use proper syntax")
print("  Use parenthesis for complex")
print("  fractions and fractional")
print("  expressions.")
print("  Enter u for unknown values")
print("")
input("    Press [Enter] to Start")
while True:
    print("")
    y = input("Enter a y value: ")
    x = input("Enter a x value: ")

    stepCount = input("Enter the number of steps: ")
    initialX = input("Enter initial x position: ")
    if (initialX != 'u'):
        finalX = input("Enter final x position: ")
        stepSize = float(stepCount)/(float(finalX) - float(initialX))
    elif (initialX == 'u'):
        stepSize = input("Step Size: ")

    x = float(x)+float(stepSize)
    y = float(y)
    derivative = input('Enter dy/dx: ')
    
    # TO DO
    # solve dy/dx to find y
    # test 

    for i in range(int(stepCount)):
        m = eval(derivative)
        print(str(m))
        # y-y0=m(x-x0)
        # y=m(x-x0)+y0
        initialEquation = (str(m) + ' * x + ' + str(eval('(x*m)+y')))
        print('')
        print('Tangent Equation ' + str(i + 1) + ': y = ' + str(initialEquation))
        y = eval(str(initialEquation))
        x = x+float(stepSize)
