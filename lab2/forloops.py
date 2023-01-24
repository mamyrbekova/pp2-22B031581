techno = {"computer", "phone", "macbook", "samsung"}
for x in techno:
    print(x)

for x in "phone":
    print(x)

# exit the loop when x is "macbook"
for x in techno:
    print(x)
    if x == "macbook":
        break

# break before the print
for x in techno:
    if x == "phone":
        break
    print(x)

# continue
for x in techno:
    if x == "samsung":
        continue
    print(x)

# range
for x in range(5):
    print(x)

# (start, end, sequence)
for x in range(2, 30, 3):
    print(x)

for x in range(6):
    print(x)
else:
    print("done!")

# if when x = 3 it breaks, then loop won't finish
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Done!")

# nested loop
adj = ["tiny", "soft"]
things = ["pillow", "hands"]

for x in adj:
    for y in things:
        print(x, y)

# pass
for x in [0, 1, 2]:
    pass



