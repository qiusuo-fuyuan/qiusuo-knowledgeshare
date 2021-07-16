'''
If you think carefully, you will know that Python decorators will be executed
during python loading of the script file.
'''
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