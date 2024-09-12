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


sorted_numbers = (lambda x: sorted(x))(nums)
print(sorted_numbers)


'''
Square each number in a list.
'''
numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)


'''
Create a lambda function that checks if a number is even.
Use this function with filter() to filter even numbers from a list.
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
