# Given a string, count the number of consonants.
# Note a consonant is a letter that is not a vowel
# i.e. a letter that is not a, e, i, o, or u.


input_str1 = "abc de"
input_str2 = "LuCiDProGrAmMiNG"

vowel = "aeiou"


# Iterative Solution
def iterative_count_consonants(input_str):
    count = 0
    for i in range(len(input_str)):
        if input_str[i].lower() not in vowel and input_str[i].isalpha():
            count += 1
    return count


# Recursive Solution
def recursive_count_consonants(input_str):
    if input_str == '':
        return 0
    if input_str[0].lower() not in vowel and input_str[0].isalpha():
        return 1 + recursive_count_consonants(input_str[1:])
    else:
        return recursive_count_consonants(input_str[1:])


print(iterative_count_consonants(input_str1))
print(iterative_count_consonants(input_str2))

print(recursive_count_consonants(input_str1))
print(recursive_count_consonants(input_str2))