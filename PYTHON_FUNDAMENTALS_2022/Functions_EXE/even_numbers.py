numbers_as_digits = [int(s) for s in input().split()]

is_even = lambda x: x % 2 == 0
even_numbers = list(filter(is_even, numbers_as_digits))

print(even_numbers)
