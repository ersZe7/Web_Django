def make_bricks(small, big, goal):
    # Calculate the maximum number of big bricks we can use
    max_big_bricks = min(big, goal // 5)
    
    # Calculate the remaining goal after using big bricks
    remaining_goal = goal - max_big_bricks * 5
    
    # Check if the remaining goal can be filled using small bricks
    return remaining_goal <= small

print(make_bricks(3, 1, 8))   # Output: True
print(make_bricks(3, 1, 9))   # Output: False
print(make_bricks(3, 2, 10))  # Output: True
