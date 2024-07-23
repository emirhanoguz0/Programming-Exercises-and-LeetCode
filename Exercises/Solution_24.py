print(str.__doc__)
print(input.__doc__)
print(print.__doc__)

def say_hello(name):
    """ Return a string says hello to the name
    Name must be a string """
    return f"Hello, {name}"

print(say_hello("Jack"))
print(say_hello.__doc__)