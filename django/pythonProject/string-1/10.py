def non_start(a, b):
    return a[1:] + b[1:]

print(non_start('Hello', 'There'))  # Output: 'ellohere'
print(non_start('java', 'code'))    # Output: 'avaode'
print(non_start('shotl', 'java'))   # Output: 'hotlava'
