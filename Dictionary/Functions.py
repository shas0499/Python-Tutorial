d = {
    "name": "Dictionary",
    "Fees": 1000,
    "Duration": "2 months",
    "Trainer": "Shaswata",
    "Location": "Kolkata",
    "Timing": "7pm to 9pm"
}

c = d.get("name")
print(c)

for key in d.keys():
    print(key)

for value in d.values():
    print(value)

for key, value in d.items():
    print(key, " : ", value)

del d["Fees"]
print(d)

i = d.pop("Duration")
print("Deleted Item is : ", i)
print(d)

new_d = dict(Course="Python", Fees=2000, Duration="3 months")
print(new_d)

new_d.update({"Fees": 2500 })
print(new_d)

new_d1 = {"Course": "Java",
          "Fees": 3000,
          "Duration": "4 months"
        }
print(new_d1)
new_d1.clear()
print(new_d1)

print(new_d)
new_d["Description"] = "This is a Python Course"
print(new_d)

print('Thank You...')