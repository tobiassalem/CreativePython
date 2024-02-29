# This is a sample Python script.

# Press Skift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from datetime import datetime


def print_hi(name, age= 0):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}, nice to meet you! Your age is {age} (or will be this year).')  # Press Ctrl+F8 to toggle the breakpoint.


def ask_for_name():
    return input('What is your name? ')


def ask_for_birth_year():
    current_year = datetime.now().year
    return input(f'Current year is {current_year}. What is your birth year? ')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    user_name = ask_for_name()
    birth_year = ask_for_birth_year()
    user_age = datetime.now().year - int(birth_year)
    print_hi(user_name, user_age)

else:
    print_hi('PyCharm (called from another python-file)')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
