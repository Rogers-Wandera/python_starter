name = "Rogers"
coins = 3

print("\n" + name + " has " + str(coins) + " coins")

message = "\n%s has %s coins" % (name, coins)
print(message)

message = "\n{} has {} coins".format(name, coins)
print(message)

message = "\n{0} has {1} coins".format(name, coins)
print(message)

message = "\n{n} has {c} coins".format(n=name, c=coins)
print(message)

dictionary = {"name": "Rogers", "coins": "2"}

message = "\n{name} has {coins} coins".format(**dictionary)
print(message)

message = f"\n{name} has {coins} coins"
print(message)

message = f"\n{name.upper()} has {2*3} coins"
print(message)
