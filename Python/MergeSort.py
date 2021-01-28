import array
import argparse
from numpy import random

unsorted_array = None

def main():
    parser = argparse.ArgumentParser(description='Sorts a randomly generated array of integers')
    parser.add_argument('-l', '--length', type=int, help ='length of array to be generated')
    args = parser.parse_args()

    if args.length is None:
        print("Length of the randomly generated array was not specified, default value of 10 will be used.")
        args.length = 10

    unsorted_array = random.randint(500, size=(args.length))
    print("Unsorted Array: ", unsorted_array)
    sorted_array = merge_sort(unsorted_array)
    print("Sorted Array: ", sorted_array)


def merge_sort(array):
    if len(array) < 2:
        return array

    mid = len(array) // 2    

    left_subset = merge_sort(array[:mid])
    right_subset = merge_sort(array[mid:])

    return merge(left_subset, right_subset)

def merge(left_subset, right_subset):
    sorted_array = []
    l_iterator = r_iterator = 0
    while l_iterator < len(left_subset) and r_iterator < len(right_subset):
        if left_subset[l_iterator] < right_subset[r_iterator]:
            sorted_array.append(left_subset[l_iterator])
            l_iterator += 1
        else:
            sorted_array.append(right_subset[r_iterator])
            r_iterator += 1
    
    while l_iterator < len(left_subset):
        sorted_array.append(left_subset[l_iterator])
        l_iterator += 1
    
    while r_iterator < len(right_subset):
        sorted_array.append(right_subset[r_iterator])
        r_iterator += 1

    return sorted_array

if __name__ == "__main__":
    main()