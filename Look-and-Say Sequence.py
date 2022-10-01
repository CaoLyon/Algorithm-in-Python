def next_number(s):
    result = []
    i = 0
    while i < len(s):
        count = 1
        while s[i] == s[i + 1] and i + 1 < len(s):
            count += 1
            i += 1
        result.append(str(count) + s[i])
        i += 1
    return ''.join(result)

print(next_number('1'))