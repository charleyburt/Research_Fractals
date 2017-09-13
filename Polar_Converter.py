#Title: Polar Converter
#Author: Charley Burtwistle
#Last Updated: September 13, 2017

import csv

def cartesian_to_polar():

    input_file = input("Enter file path: ")

    with open(input_file) as cartesian_file:
        reader = csv.reader(cartesian_file)
        for count, (c1, c2) in enumerate(reader):
            with open ('results/polar_results' + "triangle_polar" + "_iterations_.csv", 'w') as polar_file:
                theta = c1
                r = c2
                polar_file.write('{},{} \n'.format(theta , r))


if __name__ == "__main__":
    cartesian_to_polar()
