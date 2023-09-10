def add_total(num):
    if (num >= 9):
        return num + 1

    total = num + 1
    print(total)
    return add_total(total)


# sum = add_total(1)
# print(sum)

num = 0
condition = True

while condition:
    num += 1
    print(num)
    if (num == 5):
        condition = False
        break
    else:
        continue
