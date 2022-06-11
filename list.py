for x in range(6):
    print(x)
else:
    print("Finally finished!")


adj = ["red", "big", "tasty"]
fruits = ["apple", "banna", "chery"]


for x in adj:
    for y in fruits:
        print(x, y)


# Lenth of Lists


rony = ["Naimur", "Rony", "Rohima"]


print(len(rony))
# Type


print(type(rony))

# Acces In to List


print(rony[1])


# print(rony(-1))


# Change list item;


rony[1] = "Fuker"

print(rony)


# Add elements to Lists


rony.append("Added")
print(rony)


rony.insert(2, "GGGGGGGG")
print(rony)
