# create a new exception class called "MathematicalError" from BaseException class
class MathematicalError(Exception):
  pass


# write a function called parse_input that parses all the user input according to rules list defined in the exercise text
def parse_input(user_input):
  parsed_input = user_input.split()
  if len(parsed_input) != 3:
    raise MathematicalError("Invalid number of arguments")
  [n1, op, n2] = parsed_input

  try:
    n1_float = float(n1)
    n2_float = float(n2)
  except ValueError:
    raise MathematicalError("Expected numbers")

  if op not in ["+", "-", "*", "/"]:
  #if op != "+" and op != "-":
    raise MathematicalError("Operator not recognised, expected - or +")

  return n1_float, op, n2_float


# function calculate takes 2 integers and an operation type as an argument
def calculate(n1, op, n2):
    if op == '+':
        return n1 + n2
    if op == '-':
        return n1 - n2
    if op == '*':
        return n1 * n2
    if op == '/':
        return n1 / n2


while True:
    user_input = input('>>> ')
    if user_input == 'quit':
        break
    n1_float, op, n2_float = parse_input(user_input)
    result = calculate(n1_float, op, n2_float)
    print(result)
