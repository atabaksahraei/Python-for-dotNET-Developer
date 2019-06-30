#dicts
d = { "Berlin":123, "Helsinki":456, "Muenchen": 890 }
print (d)
print(d["Berlin"])
print(d.get("Berlin"))
print(d.get("NOPE"))

d["Friedberg"] = 100
print (d)

del d["Berlin"]
print(d)

if "Friedberg" in d: print("Friedberg matched")
if "Berlin" in d: print("Berlin matched")


# dict tupple
d = { "Berlin":123, "Helsinki":456, "Muenchen": 890 }

for key in d:
    print(key)

print (d.items())

for key, value in d.items():
    print (key + ": " + str(value))
