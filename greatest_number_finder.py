# Ask user for the 1st number input
num_one = int(input("Give me a number: "))

# Ask user for the 2nd number input
num_two = int(input("Give me the second number: "))

# Ask user for the 3rd number input
num_three = int(input("Give me the third number: "))

# Check if the 1st number is greater than both the 2nd and 3rd numbers
if num_one > num_two and num_one > num_three:
    # If true, print 1st number
    print(num_one)

# If false, go to the next condition
else:
    # Check if the 2nd number is greater than both the 1st and 3rd numbers
    if num_two > num_one and num_two > num_three:
        # If true, print 2nd number
        print(num_two)
    
    # If both of the conditions are false, go to the next condition
    else:
        # Check if the 3rd number is greater than both the 1st and 2nd numbers
        if num_three > num_one and num_three > num_two:
            # If true, print 3rd number
            print(num_three)

        # If all conditions are false, print that they're all equal
        else:
            print("They're all equal!")
