def lone_sum(a, b, c):
    if a == b == c:
        return 0
    elif a == b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    else:
        return a + b + c

print(lone_sum(1, 2, 3))  # Output: 6
print(lone_sum(3, 2, 3))  # Output: 2
print(lone_sum(3, 3, 3))  # Output: 0
