import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd


def plot():

    input_file = input("Enter file path: ")
    theta = pd.read_csv(input_file, usecols = [0])
    r = pd.read_csv(input_file, usecols = [1])

    #plt.axes(polar = True)
    plt.scatter(theta*np.pi/180,r,marker=',',s=1)

    plt.show()

if __name__ == "__main__":
      plot()
