# An hourglass in A is a subset of values from a 2D array 
# An hourglass sum is the sum of an hourglass' values

#Task:
# Print the largest (maximum) hourglass sum found in a given 2D array

#Parameters:
# NxN array of integers
# Returns an intger that is the maximum hourglass sum

#Plan
# Iterate over the given array DONE
# Find every hourglass
# Calculate each hourglass sum
# Find the largest hourglass sum 



#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):

#Define an empty array, this will store all the hourglassSums we find
hourglassSum = []

    #Define a nested for loop to access the 2D arrays inner values
    for i in range(6):
        for j in range(6):
            #How to define an hourglass ?
            #3 consecutive values from the 1st array
            #The value with the same indice as the 2nd value 
            #3 consecutive values from the 3rd array (same indices)
            hourglassSum = sum(innerArray[0:3]) + arr[1][1] + sum(arr[2][0:3])
            print(hourglassSum)


            #return the 1st hourglass sum: -63

            














#Example array: arr = [[-9, -9, -9, 1, 1, 1], [0, -9, 0, 4, 3, 2], [-9, -9, -9, 1, 2, 3], [0, 0, 8, 6, 6, 0], [0, 0, 0, -2, 0, 0], [0, 0, 1, 2, 4, 0]]




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    #print(result) # Print the largest (maximum) hourglass sum found in a given 2D array

    fptr.write(str(result) + '\n')

    fptr.close()
