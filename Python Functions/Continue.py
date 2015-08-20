chosenNumbers = [19, 25, 14, 2, 6, 9, 10]
print("These are the numbers to choose from.")

for n in range(1, 25):
    if n in chosenNumbers:
        continue
    print(n)


# Continue will cycle through the loop and print all numbers that are not in the  chosenNumbers list.
