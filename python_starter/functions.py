# functions

def sum(num, num2):
    if type(num) is not int or type(num2) is not int:
        return
    return num + num2


sumnums = sum(3, "4")
print(sumnums)


def multiple(*args):
    for arg in args:
        if arg == "Rogers".lower():
            print(f"Please {arg} is a reserved key word")
            continue
        else:
            print(arg)


multiple("rogers", "wandera")


def namedMultiple(**kwargs):
    print(kwargs)


namedMultiple(lastname="Rogers", firstname="Wandera")
namedMultiple(age=23, id=30)
