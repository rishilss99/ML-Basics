choice = True
while(choice):
    try:
        a = int(input("Number daal"))
        print(1/a)
        choice = False
    except ZeroDivisionError:
        print("Gaandu zero kyu daala")
        choice = True
        continue
    except ValueError:
        print("Kuchh toh daalta")
        choice = True
        continue

