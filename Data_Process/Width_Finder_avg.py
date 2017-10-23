#Title: Width Finder
#Author: Charley Burtwistle
#Last Updated: September 21, 2017


# import
import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#needed in order to specify which element to sort by
def keyfinder(elem):
    return elem[0]

#width finder method
def width_finder():

    output_theta = []
    output_r = []

    #initialize variables
    width_sum = 0.0
    degrees = 3
    current = 0
    new_list = []
    tot_samples = 0
    degree = 0



    #choose the input file
    input_file = input("Enter file path: ")

    #Open the input file
    with open(input_file) as all_points:

        #Crete Reader
        reader = csv.reader(all_points, delimiter=',')

        #Populate a List with data from file
        List = [[float(row[0]), float(row[1])] for row in reader]

    #Sort the list by degree
    List.sort(key=keyfinder)

    #Get the Max Degree in the list
    max_degree = max(m[0] for m in List)

    #For small iterations sometimes the max degree recorded is much less than 360
    #The max_degree variable makes sure we dont go too far
    print(max_degree)


    #Go through all the degrees
    while degree < max_degree:

        #go through all the degrees less than the current degree
        while (float(List[current][0]) < degree):
            #add them to a new list
            new_list.append(List[current][1])
            #delete them from the old list
            del(List[current])

        #if there is something in the list (again, mainly only used for small iterations)
        if len(new_list) != 0:
            #get the max and add it to the sum
            avg_r = sum(new_list) / float(len(new_list))
            width_sum = width_sum + avg_r

            #add the point to lists to output
            output_theta.append(degree*np.pi/180)
            output_r.append(avg_r)

            #clear the new list
            new_list = []
            #Keep track of how many samples have been taken (used to get average)
            tot_samples = tot_samples + 1

        #THIS IS WHERE YOU CAN CHOOSE HOW PRECISE TO BE
        degree = degree + 1

    #Print the average
    print(width_sum/tot_samples)
    plt.axes(polar = True)
    plt.scatter(output_theta,output_r,marker=',',s=1)
    plt.show()




#To run from command line
if __name__ == "__main__":
    width_finder()
