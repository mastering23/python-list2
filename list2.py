users = [
  ["Alex", 4],
  ["Mark", 2],
  ["Peter", 5],
  ["Marie", 1],
  ["Jessica", 3]
]


names =[]
for user in users:
    names.append(user[0])
print(names)

names2=[user[0] for user in users]
print(names2)

#filter
names3=[user for user in users if user[1] > 2]
print(names3)
print("\n----------------- MAP & Filter -------------------\n")
names4 = list(map(lambda user: user[0], users))
print(names4)

namesFilter = list(filter(lambda user: user[1] > 2, users))
print(namesFilter)

print("\n----------------- tuples -------------------\n")
#tuples can't be modify
numbers = (1,2,3,4,5,6) + (4,3,1,2)
print(numbers)

print("\n----------------- set -------------------\n")
primer = {1,1,2,2,3,4,5,6,1}
print(primer)
#sets removed duplications

set1 = {1,2,3,1,1,2}
set2 = {2,1,2,5,6,4}
print(set1 | set2) #union set
print(set1 & set2)#intersetion return match numbers for both set1 and set2
print(set1 - set2)#different return different between both sets
print(set1 ^ set2)#Simetric Different return match different numbers in both sets

print("\n----------------- Dictionary -------------------\n")
#dic use string keywords in other to access the value.
punto = {"x":25,"y":50}

print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 25

print(punto)

print(punto.get("x"))
print(punto.get("ValueDontExist",97))
