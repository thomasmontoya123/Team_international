def type_validation(in_types: list, decorating_class=False):
    """validates that all the arguments in a function call are the type they are supposed to be

    Args:
        in_types (list): Expetected argument types
        decorating_class (bool, optional): Flag to specify if we are decorating a class method or a function. Defaults to False.
    """
    def decorator(function):
        def wrapper(*args, **kwargs):
            args_check = list(args[1:] if decorating_class else args)
            if len(args_check) != len(in_types):
                raise ValueError(
                    "provide the same amount of arguments and types for a real validation")
            to_validate = list(zip(args_check, in_types))
            for check in to_validate:
                if type(check[0]) != check[1]:
                    raise TypeError(
                        f"Argument '{check[0]}' must be {check[1]}")
            return function(*args, **kwargs)
        return wrapper
    return decorator
