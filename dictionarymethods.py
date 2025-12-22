info = {
    "name" : "Ayush",
    "age" : 19,
    "marks" : {
        "phy" : 98,
        "chem" : 96,
        "maths" : 95,
    }
}
print(info)
print(info.keys())
print(len(info))
print(list(info.values()))
print(info.get("age"))
info.update({"gender" : "male"})
print(info)