word = 'word'

wordLength = (lambda x: len(x))(word)
print(wordLength)

nums = [2, 3, 4, 7, 5]

def sort_numbers(numbers):
    return (lambda x: sorted(x))(nums)


print(sort_numbers(nums))
