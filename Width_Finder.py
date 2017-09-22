#Title: Width Finder
#Author: Charley Burtwistle
#Last Updated: September 21, 2017

import csv

def keyfinder(elem):
    return elem[0]

def width_finder():
    width_sum = 0.0
    degrees = 360
    current = 0
    #clear the new list
    new_list = []


    input_file = input("Enter file path: ")
    with open(input_file) as all_points:
        reader = csv.reader(all_points)
        List = []
        for rows in reader:
            List.append(rows)

    #sort list
    List.sort(key=keyfinder)

    #go through every degree
    for degree in range(degrees):



        #go through the list
        while (float(List[current][0]) < degree):      #while the elements are still less than the current degree
            new_list.append(float(List[current][1]))      #add the radius to a new list
            del(List[current])             #delete them from the old list
            current = current + 1

        if new_list:
            width_sum = width_sum + max(new_list)
            new_list = []
            current = 0





    print(width_sum/degrees)


if __name__ == "__main__":
    width_finder()
