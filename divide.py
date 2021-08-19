def divide(a, b):
    try:
        result = a/b
    except (ZeroDivisionError, KeyError) as err:
        print('something went wrong')
        print(err)
    except TypeError as err:
        print("a and b must be ints or floats")
        print(err)
    else:
        print(f"{a} divided by {b} is equal to {result}")

divide(1,2)
