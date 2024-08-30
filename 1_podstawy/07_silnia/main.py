def sum_of_integers(N: int) -> int:
    """Return the sum of all integers from 1 to N."""
    
    return 1 if N == 0 else sum(range(1, N+1))


print(sum_of_integers(0))
print(sum_of_integers(3))
print(sum_of_integers(5))
