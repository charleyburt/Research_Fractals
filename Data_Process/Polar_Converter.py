#Title: Polar Converter
#Author: Charley Burtwistle
#Description:
        # This program takes a file of cartesian coordinates as an input.
        # It then converts these coordinates to polar coordinates.
        # It then outputs the polar coordinates to a csv file.
#Last Updated: October 10, 2017

#imports
import csv
import numpy as np

#method
def cartesian_to_polar():

    #Ask User for input and output file
    input_file = input("Enter file path: ")
    input_name = input("What would you like to name the output file: ")

    #Open files
    with open ('../results/polar_results/' + input_name + ".csv", 'w') as polar_file:
        with open(input_file) as cartesian_file:

            #Create reader
            reader = csv.reader(cartesian_file)

            #Go through input file
            for count, (x_string, y_string) in enumerate(reader):

                #Get current (x,y) point
                x_float = float(x_string)
                y_float = float(y_string)


                #Find the angle of the (x,y)
                if(x_float > 0 and y_float > 0):
                    theta = np.arctan(y_float/x_float)
                if(x_float > 0 and y_float < 0):
                    theta = np.arctan(y_float/x_float) + 2*np.pi
                if(x_float<0 and y_float>=0):
                    theta = np.arctan(y_float/x_float) + np.pi
                if(x_float<0 and y_float<0):
                    theta = np.arctan(y_float/x_float) + np.pi
                if(x_float==0 and y_float>0):
                    theta = np.pi/2
                if(x_float==0 and y_float<0):
                    theta = (3*np.pi)/2
                if(x_float==0 and y_float==0):
                    theta = "undefined"

                #convert from radians to degrees
                degrees = (theta*180)/np.pi
                #Find radius
                r = np.sqrt((x_float**2)+(y_float**2))

                #write the points to the file as (theta,r)
                polar_file.write('{},{} \n'.format(float(degrees) , float(r)))

#To run file from command line
if __name__ == "__main__":
    cartesian_to_polar()
