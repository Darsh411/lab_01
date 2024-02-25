def print_triangle_pattern(rows):
    for i in range(1, rows + 1):
        print("*" * i)

# Get user input for the number of rows in the pattern
num_rows = int(input("Enter the number of rows for the pattern: "))

# Print the triangle pattern
print_triangle_pattern(num_rows)
