users = ["Rogers", "Cathy", "Ngabwa"]
numbers = [1, 2, 3, 4, 5]
print(users[0])
print(users[1])
print(users[-3:])
print("Rogers" in users)
users.append("Baby")
print(users)
users += ['Lemi']
print(users)

users.extend(["Ryan", "Bobby"])
print(users)
print(users.index("Ryan"))

users.insert(0, "Wandera")
print(users)
users[4:7] = ["Mathew", "Lemi", "Ryan", "Bobby"]
print(users)

users.remove("Bobby")
print(users)

users.pop()
print(users)

del users[-2]
print(users)

# del numbers
numbers.clear()
print(numbers)

if "Cathy" in users:
    indexCathy = users.index("Cathy")
    users[indexCathy] = "cathy"

print(users)
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

print("WANDERA".replace("A", "O").lower())

# creating copies
newUsers = users.copy()
newUsersx = list(users)
newUsersZ = users[:]

# tuples
mytuple = tuple((1, 2, 3, 4, 5))
print(mytuple)
myAnothertuple = (5, 6, 7, 8, 9, 10)
print(type(myAnothertuple))
mynewList = list(myAnothertuple)
mynewList.append(11)
print(mynewList)
mynewtuple = tuple(mynewList)
print(mynewtuple)

# unpack tuple
(one, *two, three) = mynewtuple
print(one)
print(two)
print(three)
