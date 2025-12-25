#empty dictionary
a = {}

x = int(input("enter your physics marks -"))
a.update({"physics" : x})
y = int(input("enter your chem marks -"))
a.update({"chem" : y})
z = int(input("enter your maths marks -"))
a.update({"maths" : z})

print(a)