#Title: Polar Converter
#Author: Charley Burtwistle
#Last Updated: September 13, 2017

import csv
import numpy as np

def cartesian_to_polar():

    input_file = input("Enter file path: ")
    input_iterations = input("How many iterations: ")
    with open ('results/polar_results/POLAR_' + input_iterations + "_iterations_.csv", 'w') as polar_file:
        with open(input_file) as cartesian_file:
            reader = csv.reader(cartesian_file)
            for count, (x_string, y_string) in enumerate(reader):
                x_float = round(float(x_string),5)
                y_float = round(float(y_string),5)
                if(x_float > 0):
                    theta = np.arctan(y_float/x_float)
                if(x_float<0 and y_float>=0):
                    theta = np.arctan(y_float/x_float) + np.pi
                if(x_float<0 and y_float<0):
                    theta = np.arctan(y_float/x_float) - np.pi
                if(x_float==0 and y_float>0):
                    theta = np.pi/2
                if(x_float==0 and y_float<0):
                    theta = (3*np.pi)/2
                if(x_float==0 and y_float==0):
                    theta = "undefined"

                degrees = (theta*180)/np.pi
                r = np.sqrt((x_float**2)+(y_float**2))

                polar_file.write('{},{} \n'.format(degrees , r))


if __name__ == "__main__":
    cartesian_to_polar()
