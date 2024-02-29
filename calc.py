def print_sum(first, second):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Sum: {first + second}')  # Press Ctrl+F8 to toggle the breakpoint.


def print_diff(first, second):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Difference: {abs(first - second)}')  # Press Ctrl+F8 to toggle the breakpoint.


first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))
print(first, "and", second)
print_sum(first, second)
print_diff(first, second)
