def addNumbers(**kwargs):
    total = 0
    for key in kwargs:
        # if type(kwargs[key]) != int:
        #     return "Please all arguments must be integers"
        if not isinstance(kwargs[key], int):
            return "Please all arguments must be integers"

    for key in kwargs:
        total += kwargs[key]

    return total
