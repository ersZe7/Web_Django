def round10(num):
    if num % 10 >= 5:
        return num + (10 - num % 10)
    else:
        return num - (num % 10)

def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)

print(round_sum(16, 17, 18))  # Output: 60
print(round_sum(12, 13, 14))  # Output: 30
print(round_sum(6, 4, 4))     # Output: 10
