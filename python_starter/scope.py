# global scope
name = "Rogers"
color = "Blue"


def user():
    # local scope
    color = "Green"
    print(color)


user()
# global scope so it will still print the color Blue
print(color)


def another():
    color = "Purple"

    def inside(name):
        # nonlocal color
        color = "Red"
        print(color)
        print(f"Hello {name}")
    inside("Rogers")
    print(color)


another()
print(color)

count = 0


def calculate():
    global count
    count += 1
    if (count >= 5):
        return count + 1
    print(count)
    calculate()


calculate()
print(count)
