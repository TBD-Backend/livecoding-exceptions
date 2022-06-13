
def add_two_numbers(number_1, number_2):
    class AddTwoNumbersError(Exception):
        pass

    result = None

    if type(number_1) != int:
        raise AddTwoNumbersError(f"{number_1} is not of type int")
    if type(number_2) != int:
        raise AddTwoNumbersError(f"{number_2} is not of type int")

    return result

print(add_two_numbers(2, "adasd"))

print("The program has successfully run")