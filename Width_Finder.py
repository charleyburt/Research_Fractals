#Title: Width Finder
#Author: Charley Burtwistle
#Last Updated: September 21, 2017

import csv

def width_finder():
    width_sum = 0.0
    degrees = 360
    closest = 10
    difference = 10
    theta = 0
    r = 1
    average_width = 0
    check = 0
    value = 0


    input_file = input("Enter file path: ")
    with open(input_file) as all_points:
        reader = csv.reader(all_points)
        List = []
        for rows in reader:
            List.append(rows)

    #for every degree (0-360)
    for curr_degree in range(degrees):

        #go through every element in the list
        for all_degrees in range(len(List)-1):
            #get the difference
            difference = abs(curr_degree - float(List[all_degrees][theta]))
            #find the smallest difference
            if (difference <= closest):
                #set the smallest difference
                closest = difference
                value = all_degrees
        width_sum = width_sum + float(List[value][r])
        check = check + 1

    average_width = width_sum / degrees
    print(average_width)
    print(check)

if __name__ == "__main__":
    width_finder()
