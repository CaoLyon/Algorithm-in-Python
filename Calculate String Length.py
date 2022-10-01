# Given s string, calculate the length of the string.

input_str = 'LucidProgramming'

# Built-in function
print(len(input_str))

# Iterative Solution
def iterative_str_len(input_str):
    count = 0
    for i in input_str:
        count += 1
    return count


# Recursive Solution
def recursive_str_len(input_str):
    if input_str == '':
        return 0
    return 1 + recursive_str_len(input_str[1:])


print(iterative_str_len(input_str))
print(recursive_str_len(input_str))