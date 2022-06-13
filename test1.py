
def add_two_numbers(number_1, number_2):
    result = None

    try:
        result = int(number_1) / int(number_2)
    except ValueError:
        return 34
    finally:
        print("the finally block")

    return result

print(add_two_numbers(2, "adasd"))

print("The program has successfully run")