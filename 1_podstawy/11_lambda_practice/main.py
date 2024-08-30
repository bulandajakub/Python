'''
Create a lambda function that takes a string as input and returns the length of the string.
'''
word = 'word'

wordLength = (lambda x: len(x))(word)
print(wordLength)


'''
Given a list of numbers, use a lambda function with sorted() to sort the numbers in descending order.
'''
nums = [2, 3, 4, 7, 5]

def sort_numbers(numbers):
    return (lambda x: sorted(x))(nums)


print(sort_numbers(nums))


'''
Write a lambda function that takes two numbers as input and returns their product.
Use this function with map() to square each number in a list.
'''


'''
Create a lambda function that checks if a number is even.
Use this function with filter() to filter even numbers from a list.
'''


'''
Combine map, filter, and reduce with lambda expressions to calculate the product of even numbers in a list.
'''
