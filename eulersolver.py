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

    x = float(x)
    y = float(y)
    derivative = input('Enter dy/dx: ')
    print('')

    for i in range(int(stepCount)):
        m = eval(derivative)
        print("Slope: " + str(m))

        print("y - " + str(y) + " = " + str(m) + "(x - " + str(x) + ")")
        initialEquation = (str(m) + ' * x + ' + str(eval('(-x*m)+y')))

        x = x+float(stepSize)
        y = eval(str(initialEquation))
        
        print('Tangent Equation ' + str(i + 1) + ': y = ' + str(initialEquation))
        print("Y Coordinate after " + str(i+1) + " step(s): " + str(y))
        print('')
