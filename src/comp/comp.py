# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]
# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:") # Works
first_let = ["D"]
a = [i.name for i in humans if (i.name[0] in first_let)]
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:") # Works
last_let = "e"
b = [i.name for i in humans if(i.name[-1] in last_let)]
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:") # Works
let_between = "C, D, E, F, G"
c = [i.name for i in humans if(i.name[0] in let_between)]
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:") # Works
#increments = [29, 42, 47, 40, 36, 28, 52, 22, 52, 41]
d = []
for i in humans[:]:
    i = i.age + 10
    d.append(i)
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:") # Works
e = []
for i in humans[:]:
    e.append(f"{i.name}-{i.age}")

print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:") # Doesn't Work
f = []

for i in humans[:]:
    if i.age == 27:
        f =((f"{i.name}, {i.age}"))
    elif i.age == 28:
        f.append((f"{i.name}, {i.age}"))
    elif i.age == 29:
        f.append((f"{i.name}, {i.age}"))
    elif i.age == 30:
        f.append((f"{i.name}, {i.age}"))
    elif i.age == 31:
        f.append((f"{i.name}, {i.age}"))
    elif i.age == 32:
        f.append((f"{i.name}, {i.age}"))
        
f = tuple(f)
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:") # Works
g = []
for i in humans[:]:
    name = i.name.upper()
    g.append((f"{name}, {i.age}"))
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:") # Doesn't Work
import math
h = []
for i in humans:
    
    h.append(math.sqrt(i.age))
print(h)
