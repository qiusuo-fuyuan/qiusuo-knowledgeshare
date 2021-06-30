def uppercase_decorator(function):
    print("decorator being executed")
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


@uppercase_decorator
def say_hi():
    return 'hello there'

say_hi()