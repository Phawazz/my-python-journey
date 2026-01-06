while True:
    try:
        numtype = int(input("Enter a whole number here: "))
        if numtype % 2 == 0:
            print("Even")
        else:
            print("Odd")
        break
    except ValueError:
        print("Invalid input. Please enter a whole number")