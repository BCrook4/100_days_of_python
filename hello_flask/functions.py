def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1 * n2

# functions are first class objects, can be passed around as arguments like other variable types e.g. int/string/float

def calculate(operation, n1, n2):
    return operation(n1, n2)

print(calculate(subtract, 2, 3))

# functions can be nested in other functions

# def outer_function():
#     print("I'm outer")
#
#     def nested_function():
#         print("I'm inner")
#
#     nested_function()
#
# outer_function()

# functions can return other functions

def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    return nested_function

# the nested function is returned by the outer_function which can then be stored as a variable
inner_function = outer_function()
# once stored, we can then call the function by adding the parenthesis
inner_function()