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
    degrees = 3
    current = 0
    new_list = []
    tot_samples = 0
    degree = 0
    test = 0


    #choose the input file
    input_file = input("Enter file path: ")
    with open(input_file) as all_points:                    #open it
        reader = csv.reader(all_points, delimiter=',')                     #create reader
        List = [[float(row[0]), float(row[1])] for row in reader]
        # List = []                                        #create list
        # for rows in reader:                                 #populate list
        #     List.append(rows)

    List.sort(key=keyfinder)                                #sort list
    max_degree = max(m[0] for m in List)
    print(max_degree)


    while degree < max_degree:
        while (float(List[current][0]) < degree):
            new_list.append(List[current][1])
            del(List[current])
        test = test + 1

        if len(new_list) != 0:
            width_sum = width_sum + float(max(new_list))
            new_list = []
            tot_samples = tot_samples + 1


        degree = degree + 0.5


    print(width_sum/tot_samples)
    print(tot_samples)
    print(test)



    # #go through every degree (0-360)
    # for degree in range(degrees):
    #
    #     #go through the list
    #     while (List[current][0] < degree):         #while the elements are still less than the current degree
    #         new_list.append(float(List[current][1]))        #add the radius to a new list
    #         del(List[current])                            #delete them from the old list
    #         current = current + 1
    #
    #     #if the new_list exists
    #     if new_list:
    #         width_sum = width_sum + max(new_list)           #add the max of the new list (all radii for current angle) to the sum
    #         tot_samples =  tot_samples + 1
    #         new_list = []                                   #clear the new list
    #         curr_elem = 0                                   #reset curr_elem
    #
    #     degree = degree + 1
    #
    # print(width_sum/degrees)
    # print(tot_samples)


if __name__ == "__main__":
    width_finder()
