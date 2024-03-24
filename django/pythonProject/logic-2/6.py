def close_far(a, b, c):
    def is_close(x, y):
        return abs(x - y) <= 1
    
    def is_far(x, y, z):
        return abs(x - y) >= 2 and abs(x - z) >= 2
    
    if (is_close(a, b) and is_far(a, b, c)) or (is_close(a, c) and is_far(a, c, b)):
        return True
    else:
        return False
    
print(close_far(1, 2, 10))  # Output: True
print(close_far(1, 2, 3))   # Output: False
print(close_far(4, 1, 3))   # Output: True

