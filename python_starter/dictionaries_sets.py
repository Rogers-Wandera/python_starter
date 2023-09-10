person = {
    "id": 23,
    "username": "Wandera Rogers",
    "address": "Nkumba"
}

person2 = dict(id="24", username="Ngabwa Catherine", address="Nkumba")

print(person)
print(person2)

print(person['address'])
print(person2.get("username"))

person2['age'] = 22
print(person2)

print(person.keys())
print(person.values())

print(person.items())
print("username" in person)

person.update({"status": "married"})
print(person)

person['status'] = "single"
print(person)

# remove item
print(person.pop("status"))
print(person)

person['status'] = "married"
print(person.popitem())
print(person)

person['status'] = "married"
print(person)
del person['status']
print(person)

person2.clear()
print(person2)

personCopy = person.copy()
personCopy['hobbies'] = ["Football", "Movies"]
print(person)
print(personCopy)


# nested dictionary
student = {
    "studentNo": "2100101040",
    "CGPA": 4.5
}

student2 = {
    "studentNo": "2100101050",
    "CGPA": 5.0
}

students = {
    "student1": student,
    "student2": student2
}
print(students)
print(students["student1"]['studentNo'])


# sets
nums = {1, 2, 3, 4, 5}
nums2 = set((3, 4, 5, 6, 7, 90))
print(nums)
print(nums2)

# no duplicates
nums3 = {1, 1, 2, 3, 4, 5, 6, 7, 7, 9, 8, 9, 8, 80}
print(nums3)

# true in set is 1 and false is 0
nums4 = {1, True, 3, 5, 6, 7, 8, False, 0}
print(nums4)

print(True in nums4)

# addig elements in a set
nums.add(20)

# adding elements of another set in a set
nums.update(nums4)
print(nums)

# create a set from two or more sets
unionSet = nums.union(nums2, nums3)
print(unionSet)

one = {1, 2, 3, 4, 5}
two = {1, 3, 6, 7, 2}

# get only the dupliactes in the two sets
dupliactes = one.intersection(two)
print(dupliactes)

ones = {1, 2, 3, 4, 5}
twos = {1, 3, 6, 7, 2}

# update ones to only have the duplicates
ones.intersection_update(twos)
print(ones)

ones = {1, 2, 3, 4, 5}
twos = {1, 3, 6, 7, 2}

# get only the elements that are not duplicates
noDuplicates = ones.symmetric_difference(twos)
print(noDuplicates)

# make ones only have everything except the duplicates
ones.symmetric_difference_update(twos)
print(ones)
