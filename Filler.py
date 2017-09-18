#Title: Fill in Gaps
#Author: Charley Burtwistle
#Last Updated: September 17, 2017

import csv
import numpy as np

def fill_in_gaps():

    input_file = input("Enter file path: ")
    input_iterations = input("How many iterations: ")
    with open ('results/full_results/' + input_iterations + "_iterations_.csv", 'w') as full_file:
        with open(input_file) as cartesian_file:
            reader = csv.reader(cartesian_file)
            writer = csv.writer(full_file)
            for count, (x_string, y_string) in enumerate(reader):
                x_float = float(x_string)
                y_float = float(y_string)

                full_x = np.arange(1, 10, 0.1)
                full_y = np.arange(1, 10, 0.1)

                for x, y in zip(full_x, full_y):
                    writer.writerow([x, y])



if __name__ == "__main__":
    fill_in_gaps()
