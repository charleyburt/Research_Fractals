#Title: Koch Snowflake
#Author: Charley Burtwistle
#Last Updated: September 6, 2017


#import `turtle` to draw the fractal
from turtle import *
import time
import numpy as np



distance = 0 #create distance variable to track circumference
coordinate_list = []
moment=time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime()) #create moment

#Draws the koch curve (i.e. "one side" of the koch snowflake)
def koch_curve(side_length, iterations):   #pass in the side length and how many iterations


    if iterations == 0:    # if 0 iterations
        forward(side_length)    # draw one side
        global distance # make distance global so it can be printed out
        distance += side_length #add the side length to distance
        coordinate_list.append(position())
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

    with open ('results/Koch_Snowflake_' + moment + "_.txt", 'w') as coordinate_file:
        for coordinates in coordinate_list:
            coordinate_file.write("%s\n" % str(coordinates))




# Code to run from command line
if __name__ == "__main__":
    input_speed = int(input("How fast would you like to draw between 0-10? (0=fast, 10=slow): "))
    speed(input_speed)
    input_length = int(input("How big would you like your fractal between 100-300? (100=small, 300=big): "))
    length = input_length
    penup()
    backward(length/2.0)
    left(90)
    forward(np.sqrt((length**2)-((length/2.0)**2))/3)
    right(90)
    pendown()
    input_iterations = int(input("How many iterations? : "))
    Snowflake(length, input_iterations)
    done()
