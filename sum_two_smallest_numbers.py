import sys

def sum_two_smallest_numbers(numbers):
    #your code here
    smallest = sys.maxsize
    second_smallest = sys.maxsize
    
    for i in range(len(numbers)):
        if(numbers[i] < smallest):
            second_smallest = smallest
            smallest = numbers[i]
        elif(numbers[i] < second_smallest):
            second_smallest = numbers[i]
    
    
    return smallest + second_smallest
