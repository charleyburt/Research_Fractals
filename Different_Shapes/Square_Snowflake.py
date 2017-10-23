#Title: Square snowflake
#Author: Charley Burtwistle
#Last Updated: September 8, 2017


#import `turtle` to draw the fractal
from turtle import *


circumference = 0 #create circumference variable

#Draws one side of the fractal
def koch_curve(side_length, iterations):   #pass in the side length and how many iterations


    if iterations == 0:    # if 0 iterations
        coordinate_file.write('{},{} \n'.format(float(xcor()) , float(ycor())))
        forward(side_length)    # draw one side
        global circumference # make circumference global so it can be printed out
        circumference += side_length #add the side length to circumference
        return

    #draw the fractal

    #reduce side length by 1/3
    side_length /= 3.0

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
    speed('fastest')
    tracer(0,0)
    length = 300
    penup()
    backward(length/2.0)
    left(90)
    forward(length/2.0)
    right(90)
    pendown()
    input_iterations = int(input("How many iterations? : "))
    coordinate_file = open ('../results/cartesian_results/' + "square_" + str(input_iterations) + "_iterations_.csv", 'w')
    Snowflake(length, input_iterations)
    coordinate_file.write('{},{} \n'.format(float(xcor()) , float(ycor())))
    coordinate_file.close()
    update()
    done()
