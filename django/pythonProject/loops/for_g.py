x = int(input())

for divisor in range(2, x):
    if x % divisor == 0:
        print(divisor)
        break
