"""3.

Write a function that takes in a non-empty array of integers that are sorted in ascending order and returns a
new array of the same length with the squares of the original integers also sorted in ascending order.

Example Input:

numbers = [1,2,3,5,6,8,9]"""

numbers = [1,2,3,5,6,8,9]

def squared_function(array):
    squares = []
    for i in numbers:
        squares.append(i**2)
        squares.sort()
    return squares

squared_function(numbers)

# 4.	Write tests for the newly created Sorted Squared Numbers function (in Q3). Provide a brief explanation for your test case options.

# in test_squared.py file




#number 9 coding question

def twoNumberSum(array, targetSum):
    matches = {}
    for number in array:
        match = targetSum - number
        if match in matches:
            return [match, number]
        else:
            matches[number] = True
    return []

numbers = [3, 5, -4 ,8, 11, 1, -1, 6]
target_sum = 10

twoNumberSum(numbers,target_sum)