def add_numbers(*args):
    total = 0
    for a in args:
        total += a
    print(total)

add_numbers(7)
add_numbers(4, 12, 19)

# This function will take an unknown number of arguments *args and add them together.
# *args can be used in place of a defined argument for any unknown
