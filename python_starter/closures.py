import random


def parentFunction(name):
    # life = 100
    year = random.choices(range(0, 100))
    life = year[0]

    def lifespan():
        nonlocal life
        life -= 1
        if life > 1:
            print(f"{name} you have {life} years left")
        elif life == 1:
            print(f"{name} you only have {1} year left")
        else:
            print(f"{name} please rest with {life} years left")
    return lifespan


rogers = parentFunction("Rogers")
cathy = parentFunction("Cathy")
cathy()
