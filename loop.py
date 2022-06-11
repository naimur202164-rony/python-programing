arr = ["Naimir", "Rony", "Nila", "Nishad", ""]


for z in arr:
    print(z)


# Loop through Index Number


arrr = ["hello", "World", "Nila", "Rakib"]


for x in range(len(arrr)):
    print(arrr[x])


thislist = ["apple", "banana", "cherry"]


for i in range(len(thislist)):
    print(thislist[i])


# Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = []


for x in fruits:
    if "a" in x:
        newList.append(x)

        print(newList)
