# Define a decorator function that takes another function as its argument.
def my_decorator(func):
    # Define a wrapper function inside the decorator.
    def wrapper():
        print("Something is happening before the function is called.")
        # Call the original function that was passed to the decorator.
        func()
        print("Something is happening after the function is called.")
    # Return the wrapper function.
    return wrapper

# Define a function and apply the decorator to it using the "@" symbol.


@my_decorator
def say_hello():
    print("Hello!")


# Call the decorated function.
say_hello()
