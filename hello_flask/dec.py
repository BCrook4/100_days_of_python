## Python Decorator Function
import time

## a decorator function is just a function that wraps another function and can provide some additional functionality
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # can add something to be done before function
        function()
        # function() # could run the function again
        # or add something to be done after the function
    return wrapper_function


# say we want some additional functionality for our function like adding a delay for example
# add the @decorator before the function to use the decorator
@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")

def say_greeting():
    print("How are you?")

# say_hello()
say_greeting()

# can also use decorator without @ sign by doing the following
decorated_function = delay_decorator(say_greeting)
decorated_function()
# but using the @ sign is a more clear way of doing it