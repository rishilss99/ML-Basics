try:
    a = int(input("Enter a number"))
    print(1/a)
except ValueError:
    a = int(input("Enter a proper number"))
    print(1/a)
except ZeroDivisionError:
    a = int(input("You can't enter 0"))
    print(1/a)