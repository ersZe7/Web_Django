def fix_teen(n):
    if n in [13, 14, 17, 18, 19]:
        return 0
    return n

def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

print(no_teen_sum(1, 2, 3))   # Output: 6
print(no_teen_sum(2, 13, 1))  # Output: 3
print(no_teen_sum(2, 1, 14))  # Output: 3
