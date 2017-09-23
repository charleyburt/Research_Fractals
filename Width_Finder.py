#Title: Width Finder
#Author: Charley Burtwistle
#Last Updated: September 21, 2017


# import
import csv

#needed in order to specify which element to sort by
def keyfinder(elem):
    return elem[0]

#width finder method
def width_finder():

    #initialize variables
    width_sum = 0.0
    degrees = 360
    curr_elem = 0
    new_list = []


    #choose the input file
    input_file = input("Enter file path: ")
    with open(input_file) as all_points:                    #open it
        reader = csv.reader(all_points)                     #create reader
        List = []                                           #create list
        for rows in reader:                                 #populate list
            List.append(rows)

    List.sort(key=keyfinder)                                #sort list

    #go through every degree (0-360)
    for degree in range(degrees):

        #go through the list
        while (float(List[curr_elem][0]) < degree):         #while the elements are still less than the current degree
            new_list.append(float(List[current][1]))        #add the radius to a new list
            del(List[curr_elem])                            #delete them from the old list
            curr_elem = curr_elem + 1

        #if the new_list exists
        if new_list:
            width_sum = width_sum + max(new_list)           #add the max of the new list (all radii for current angle) to the sum
            new_list = []                                   #clear the new list
            curr_elem = 0                                   #reset curr_elem

    print(width_sum/degrees)


if __name__ == "__main__":
    width_finder()
