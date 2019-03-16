dictionary_Sander = {
    "eesnimi": "Sander",
    "perenimi": "Aru",
    "sünniaasta": 1990,
    "elukoht": "Saaremaa",
    "lemmikloom": "kass"
}

print(dictionary_Sander.get("elukoht"))

home = dictionary_Sander["elukoht"]
print(home)

dictionary_Sander["lemmikloom"] = "koer"
print(dictionary_Sander.get("lemmikloom"))

for x in dictionary_Sander:
    print(x)

for x in dictionary_Sander:
    print(dictionary_Sander[x])

for x in dictionary_Sander.values():
    print(x)

for x, y in dictionary_Sander.items():
    print(x, y)

if "elukoht" in dictionary_Sander:
    print("""Jah, elukoht on dictionary's sees.""")

print(len(dictionary_Sander))

dictionary_Sander["pikkus"] = 193
print(dictionary_Sander.get("pikkus"))

dictionary_Sander.pop("eesnimi")
for x, y in dictionary_Sander.items():
    print(x, y)

dictionary_Sander = {
    "eesnimi": "Sander",
    "perenimi": "Aru",
    "sünniaasta": 1990,
    "elukoht": "Saaremaa",
    "lemmikloom": "kass"
}

dictionary_Sander.popitem()
for x, y in dictionary_Sander.items():
    print(x, y)

dictionary_Sander = {
    "eesnimi": "Sander",
    "perenimi": "Aru",
    "sünniaasta": 1990,
    "elukoht": "Saaremaa",
    "lemmikloom": "kass"
}

del dictionary_Sander["perenimi"]
for x, y in dictionary_Sander.items():
    print(x, y)

dictionary_Sander = {
    "eesnimi": "Sander",
    "perenimi": "Aru",
    "sünniaasta": 1990,
    "elukoht": "Saaremaa",
    "lemmikloom": "kass"
}

for x, y in dictionary_Sander.items():
    print(x, y)

dictionary_Sander = {
    "eesnimi": "Sander",
    "perenimi": "Aru",
    "sünniaasta": 1990,
    "elukoht": "Saaremaa",
    "lemmikloom": "kass"
}

dictionary_Sander.clear()
for x, y in dictionary_Sander.items():
    print(x, y)

dictionary_Sander = {
    "eesnimi": "Sander",
    "perenimi": "Aru",
    "sünniaasta": 1990,
    "elukoht": "Saaremaa",
    "lemmikloom": "kass"
}