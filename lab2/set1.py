tech = {"computer", "phone", "macbook", "samsung"}
print(tech)
print(len(tech))
print(type(tech))

for x in tech:
    print(x)

print("samsung" in tech)    # output true/false

# add/update
tech.add("xiaomi")
print(tech)

tech2 = {"lenovo", "poco", "oppo", "vivo"}
tech.update(tech2)
print(tech)

# remove/discard
tech.remove("phone")
print(tech)
tech.discard("macbook")

# clear
tech.clear()
print(tech)





