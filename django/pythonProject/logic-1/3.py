def squirrel_play(temperature, is_summer):
    if is_summer:
        return temperature >= 60 and temperature <= 100
    else:
        return temperature >= 60 and temperature <= 90

print(squirrel_play(70, False))  # Output: True
print(squirrel_play(95, False))  # Output: False
print(squirrel_play(95, True))   # Output: True
