from functools import wraps
from time import sleep

def emphasize(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        return_val_from_undecorated_function = func(*args, **kwargs)

        emphasized = return_val_from_undecorated_function.upper() + "!!!"

        return emphasized

    return wrapper


def sarcastic_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        return f'Yeah totally, "{val}" that\'s hilarious'

    return wrapper


def procrastinate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sleep(4)
        return func(*args, **kwargs)
    return wrapper

def proclaim(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        return "I believe, the best summer activity is," + val

    return wrapper


@procrastinate
@proclaim
def say(txt):
    return txt

@sarcastic_decorator
@emphasize
def decompressing_activity(activity):
    return activity

if __name__ == "__main__":
    print(say('swimming in nature!'))
    