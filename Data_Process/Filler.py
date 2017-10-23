#Title: Fill in Gaps
#Author: Charley Burtwistle
#Description:
        # This program gets a file full of corners of a shape.
        # It then takes those corners, and fills in all the points in between.
        # It outputs a file full of points of the "complete" shape.
#Last Updated: September 17, 2017

#imports
import csv
import numpy as np

#method
def fill_in_gaps():

#Declare Variables
    step = 0.0      #how far each point is from eachother
    slope = 0.0     #used for filling in the points when there is a change in the x and y direction
    x_col = 0       #the column that holds our x values
    y_col = 1       #the column that holds our y values

    #THIS WILL DETERMINE HOW MANY POINTS ARE IN BETWEEN EACH POINT
    total = 1000

    #Ask user where the data is coming from/going to
    input_file = input("Enter file path: ")
    input_name = input("What would you like to name the output file: ")

    #Open the files
    with open ('../results/full_results/' + input_name + ".csv", 'w') as full_file:
        with open(input_file) as cartesian_file:

            #Create reader and writer
            reader = csv.reader(cartesian_file)
            writer = csv.writer(full_file)

            #Create empty list to fill
            csvList = []

            #Fill the list with the data from the file
            for rows in reader:
                csvList.append(rows)

            #Figure out the step and slope
            for i in range(len(csvList) - 1):
                step = (float(csvList[i+1][x_col]) - float(csvList[i][x_col]))/total
                slope = (float(csvList[i+1][y_col]) - float(csvList[i][y_col]))/(float(csvList[i+1][x_col]) - float(csvList[i][x_col]))

                #Fill in the points
                for j in range(total):
                    x_line = (float(csvList[i][x_col]) + (j * step))
                    y_line = (float(csvList[i][y_col]) + (j * step * slope))

                    #Write them to the output file
                    writer.writerow([float(x_line) , float(y_line)])


#So file can be run from command line
if __name__ == "__main__":
    fill_in_gaps()
