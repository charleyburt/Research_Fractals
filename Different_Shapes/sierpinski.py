#Title: Koch Snowflake
#Author: Kris Williams
#Maintained by: Charley Burtwistle
#Last Updated: October 10, 2017

#imports
import numpy as np
from turtle import *

distance = 0
#Draws one side
def Side(l,d):

  # If it is at the "bottom" iteration
  if(d==0):
     #Record the current point
     coordinate_file.write('{},{} \n'.format(float(xcor()) , float(ycor())))
     forward(l)    # draw one side
     global distance # make distance global so it can be printed out
     distance += l #add the side length to distance
     return

  #Recursive algorithm to draw triangle (Credit: Kris Williams)
  Side(l/2, d-1)
  diagUp(l/2)
  Side(l/2,d-1)
  diagDown(l/2)
  Side(l/2,d-1)

#Draw Diagonal
def diagUp(l):
   coordinate_file.write('{},{} \n'.format(float(xcor()) , float(ycor())))

   left(120)
   forward(l)
   right(120)

#Draw Diagonal
def diagDown(l):
   coordinate_file.write('{},{} \n'.format(float(xcor()) , float(ycor())))

   right(120)
   forward(l)
   left(120)

#To run from command line
if __name__ == "__main__":
    speed(3.4)
    tracer(0,0)
    length = 300.0
    penup()
    backward(length/2.0)
    left(90)
    forward(np.sqrt((length**2)-((length/2.0)**2))/3)
    right(90)
    pendown()
    input_iterations = int(input("How many iterations? : "))
    coordinate_file = open ('../results/cartesian_results/' + "triangle_" + str(input_iterations) + "_iterations_.csv", 'w')
    size  = 300.0
    Side(size,input_iterations)
    right(120)
    Side(size,input_iterations)
    right(120)
    Side(size,input_iterations)
    #Record the last point (same as first point)
    coordinate_file.write('{},{} \n'.format(float(xcor()) , float(ycor())))
    coordinate_file.close()
    print(distance)
    update()
    done()
