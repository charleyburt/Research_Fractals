#Title: Koch Snowflake
#Author: Charley Burtwistle
#Last Updated: October 10, 2017


#import `turtle` to draw the fractal
from turtle import *
import numpy as np

distance = 0 #create distance variable to track circumference

#Draws the koch curve (i.e. "one side" of the koch snowflake)
def koch_curve(side_length, iterations):   #pass in the side length and how many iterations


    if iterations == 0:    # if 0 iterations
        coordinate_file.write('{},{} \n'.format(float(xcor()) , float(ycor())))
        forward(side_length)    # draw one side
        global distance # make distance global so it can be printed out
        distance += side_length #add the side length to distance

        return

    #draw koch curve (this will be repeated for each iteration)

    #reduce side length by 1/3
    side_length /= 3.0

    #draw "over"
    koch_curve(side_length, iterations-1)

    #draw "up"
    left(60)
    koch_curve(side_length, iterations-1)

    #draw "down"
    right(120)
    koch_curve(side_length, iterations-1)

    #draw "over"
    left(60)
    koch_curve(side_length, iterations-1)

#Draws the koch curve 3 times (i.e. the koch snowflake)
def Snowflake(side_length, iterations):    #pass in the side length and number of iterations

    for i in range(3): #for each side of the triangle
        koch_curve(side_length, iterations) #draw the koch curve
        right(120) #move on to the next side

    print(distance) #when the entire thing is drawn, print it out






# Code to run from command line
if __name__ == "__main__":
    speed('fastest')
    #tracer(0,0)
    length = 300
    penup()
    backward(length/2.0)
    left(90)
    forward(np.sqrt((length**2)-((length/2.0)**2))/3)
    right(90)
    pendown()
    input_iterations = int(input("How many iterations? : "))
    coordinate_file = open ('../results/cartesian_results/' + "triangle_" + str(input_iterations) + "_iterations_.csv", 'w')
    Snowflake(length, input_iterations)
    coordinate_file.write('{},{} \n'.format(float(xcor()) , float(ycor())))
    coordinate_file.close()
    #update()
    done()
