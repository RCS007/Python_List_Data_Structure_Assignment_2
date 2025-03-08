# Question 2

# Enter a list of ten colours. Ask the user for a starting number between 0 and 4 and an end number
# between 5 and 9. Display the list for those colours between the start and end numbers the user input.


# List of ten colors
colors_list = ["Red", "Green", "Blue", "Yellow", "Orange", "Purple", "Pink", "Black", "White", "Brown"]

# Ask the user for a starting and an ending number
start_index = int(input("Enter a starting number between 0 and 4: "))
end_index = int(input("Enter an ending number between 5 and 9: "))

# Ensure the input indices are within the valid range
if 0 <= start_index <= 4 and 5 <= end_index <= 9:
    # Display the colors between the start and end indices
    print("Colors between the given indices:", colors_list[start_index:end_index+1])
else:
    print("Invalid input! Please ensure the starting number is between 0 and 4, and the ending number is between 5 and 9.")
