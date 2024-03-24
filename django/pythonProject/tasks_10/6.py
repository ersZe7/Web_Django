def wrap(string, max_width):
    result = ""
    
    for i in range(0, len(string), max_width):
        result += string[i:i+max_width] + "\n"
    
    return result.rstrip("\n")

s = input()
w = int(input())

print(wrap(s, w))
