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
print("  expressions. Please convert")
print("  cx to c*x when entering dy/dx")
print("")
input("    Press [Enter] to Start")
while True:
    print("")
    y = input("Enter a y value: ")
    x = input("Enter a x value: ")
    stepCount = input("Enter the number of steps: ")
    stepSize = input("Step size: ")
    derivative = input('Enter dy/dx: ')

    if (y) and (x) and (stepCount) and (stepSize) and (derivative):
        x = float(x)
        y = float(y)
        print('')

        for i in range(int(stepCount)):
            m = eval(derivative)
            print("---- Step " + str(i+1) + " ----")
            print("Slope: " + str(m))

            print("y - " + str(y) + " = " + str(m) + "(x - " + str(x) + ")")
            initialEquation = (str(m) + ' * x + ' + str(eval('(-x*m)+y')))

            x = x+float(stepSize)
            y = eval(str(initialEquation))
        
            print('Tangent Equation ' + str(i + 1) + ': y = ' + str(initialEquation))
            print("Y Coordinate after " + str(i+1) + " step(s): " + str(y))
            print('')
            if (int(i+1) < int(stepCount)):
                a = input("Press [Enter] to proceed to step " + str(i+2))
            elif (int(i+1) == int(stepCount)):
                a = input("Press [Enter] to proceed")
            print('')        
    else:
        print('Unsolvable. Double check')
        print('your inputs.')
