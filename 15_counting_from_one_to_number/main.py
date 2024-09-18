numX = int(input())

# the * operator unpacks the range object into arguments for the print function
print(*range(1, numX + 1), sep='\n')
