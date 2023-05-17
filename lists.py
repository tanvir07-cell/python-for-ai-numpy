# li = list([1, 2, 3, 4, 5])
# print(type(li))
# print(li[3])

# print(1 not in li)
# print(4 in li)


# givenCountry = list(["Bangladesh", "Canada", "France", "Saudi-Arabia"])

# useCountry = input("Enter your country name : ")

# print(useCountry in givenCountry)


# creating list and it's all properties:

li = list(range(1, 5))

# adding 5 to the last of the list:

li.append(5)

# adding 10 to the 2nd index:
li.insert(2, 10)

# remove to the given element:
li.remove(10)


# remove to the last element and returns the last element using pop() method and also modifies the original list:
five = li.pop()
print(five)


# delete entire list:
# del (li)

print(li)


# adding 2 list using extend:
siblings = ["Tanvir Rifat", "Arafat"]
parents = ["Mizanur Rahman", "Rabeya begum"]
parents.extend(siblings)
print(parents)


# siblings array er moddeh full parents er array sign soho add hoye jabe:
siblings.append(parents)
print(siblings)
