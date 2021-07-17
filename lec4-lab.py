# Create a function to give information about a two-dice role. Your function should do these three things:
# 1. If either die roll is not in between 1 and 6 inclusive print "Both dice need to be between 1 and 6!" and return nothing (None)
# 2. Print out the probability of rolling the sum of the numbers (Hint: # of possible ways to roll that sum / # of ways to roll two dice).
#    Round the probability to three decimal places. (Hint: look up the round() function)
# 3. If the user has rolled two 1s then print out "Snake eyes!

def dice_probability(die_1, die_2):
    '''
    die_1 and die_2 are both assumed to be non-negative integers
    '''
    if ...:
        ...

    s = die_1 + die_2
    if ...:
        ...
    elif ...:
        ...
    ...

#dice_probability(0, 2)
# Expected output:
# "Both dice need to be between 1 and 6!"

#dice_probability(3, 4)
# Expected output:
# 0.194

#dice_probability (1, 1)
# Expected output:
# 0.028
# "Snake eyes!"

# Write a function that takes two functions, a low float and a high float. Print out which function is larger each time
#  you increase the input value by 1 starting at the low float and ending before you exceed the high float.
def larger_function(f1, f2, low, high):
    '''
    f1 and f2 are functions that return floats
    low and high are floats that represent the range of input values into f1 and f2
    '''
    # x = ...
    # while x ...:
    #     if ...:
    #         print()
    #     else:
    #         print()
    #     x += 1

# define f1 as the sine function with amplitude 2
# def f1(x):
#     ...

# define f2 as the cosine function with shift 3
# def f2(x):
#     ...

# call your function with low = 0 and high = 4pi
# larger_function(...)
