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
            for count, (c1, c2) in enumerate(reader):
                theta = c1
                r = np.sqrt((c1**2)+(c2**2))
                polar_file.write('{},{} \n'.format(theta , r))


if __name__ == "__main__":
    cartesian_to_polar()
