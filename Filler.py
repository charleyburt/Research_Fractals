#Title: Fill in Gaps
#Author: Charley Burtwistle
#Last Updated: September 17, 2017

import csv
import numpy as np

def fill_in_gaps():

    step = 0.0
    slope = 0.0
    x_col = 0
    y_col = 1
    total = 10000

    input_file = input("Enter file path: ")
    input_name = input("What would you like to name the output file: ")
    with open ('results/full_results/' + input_name + ".csv", 'w') as full_file:
        with open(input_file) as cartesian_file:
            reader = csv.reader(cartesian_file)
            writer = csv.writer(full_file)
            csvList = []
            for rows in reader:
                csvList.append(rows)

            for i in range(len(csvList) - 1):
                step = (float(csvList[i+1][x_col]) - float(csvList[i][x_col]))/total
                slope = (float(csvList[i+1][y_col]) - float(csvList[i][y_col]))/(float(csvList[i+1][x_col]) - float(csvList[i][x_col]))
                for j in range(total):
                    x_line = (float(csvList[i][x_col]) + (j * step))
                    y_line = (float(csvList[i][y_col]) + (j * step * slope))
                    writer.writerow([float(x_line) , float(y_line)])


if __name__ == "__main__":
    fill_in_gaps()
