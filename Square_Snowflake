#Title: Square snowflake
#Author: Charley Burtwistle
#Last Updated: September 8, 2017


#import `turtle` to draw the fractal
from turtle import *


circumference = 0 #create circumference variable

#Draws one side of the fractal
def koch_curve(side_length, iterations):   #pass in the side length and how many iterations


    if iterations == 0:    # if 0 iterations
        forward(side_length)    # draw one side
        global circumference # make circumference global so it can be printed out
        circumference += side_length #add the side length to circumference
        return

    #draw the fractal

    #reduce side length by 1/4
    side_length /= 4.0

    #draw "over"
    koch_curve(side_length, iterations-1)

    #draw "up"
    left(90)
    koch_curve(side_length, iterations-1)

    #draw "over"
    right(90)
    koch_curve(side_length, iterations-1)

    #draw "down"
    right(90)
    koch_curve(side_length, iterations-1)

    #draw "over"
    left(90)
    koch_curve(side_length, iterations-1)

#Draws the koch curve 4 times (i.e. the square snowflake)
def Snowflake(side_length, iterations):    #pass in the side length and number of iterations

    for i in range(4): #for each side of the square
        koch_curve(side_length, iterations) #draw the side of the fractal
        right(90) #move on to the next side

    print(circumference) #when the entire thing is drawn, print out the circumference drawn



# Code to run from command line
if __name__ == "__main__":
    input_speed = int(input("How fast would you like to draw between 0-10? (0=fast, 10=slow): "))
    speed(input_speed)
    input_length = int(input("How big would you like your fractal between 100-300? (100=small, 300=big): "))
    length = input_length
    penup()
    backward(length/2.0)
    pendown()
    input_iterations = int(input("How many iterations? : "))
    Snowflake(length, input_iterations)
    done()
