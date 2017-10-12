import numpy as np
import csv

def circle_generator():

    with open ("./circle_points.csv", 'w') as full_file:

        writer = csv.writer(full_file)

        #Create empty list to fill
        csvList = []


        for j in range(360):
            theta = j
            r = 1

            #Write them to the output file
            writer.writerow([theta,r])

if __name__ == "__main__":
    circle_generator()
