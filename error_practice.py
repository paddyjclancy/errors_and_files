
while True:
    try:
        x = int(input("Please enter a number:  "))
        if x <= 10:
            break
        elif x > 10:
            raise Exception("Number too high")
    except ValueError:
        print("That is not an integer")

# while True:
#     try:
#         x = int(input("Please enter a number:  "))
#         break
#     except ValueError:
#         print("That is not an integer")
