name_to_age = {"Bill": 21, "Jane": 4, "Sven": 56, "Mario":24}
name = input("What is your name? ")
age = input("How old are you? ")

name_to_age[name] = age
for name, age in name_to_age.items():
    print(name, ":", age)

key = name_to_age.keys()
print(f"{name}")
print(key)

value = name_to_age.values()
print(value)


