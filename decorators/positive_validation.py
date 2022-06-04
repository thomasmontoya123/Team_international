def positive_validation(decorating_class=False):
    """validates that all the arguments in a function call are positive

    Args:
        decorating_class (bool, optional): Flag to specify if we are decorating a class or a function. Defaults to False.
    """
    def decorator(function):
        def wrapper(*args, **kwargs):
            args_check = args[1:] if decorating_class else args
            for arg in args_check:
                if arg < 0:
                    raise ValueError(
                        f"Number '{arg}' most be a positive integer")
            return function(*args, **kwargs)
        return wrapper
    return decorator
