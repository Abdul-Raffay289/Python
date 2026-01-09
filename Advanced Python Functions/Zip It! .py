s1 = [1, 2, 3]
s2 = ['b', 'a', 'c']
s3 = list(zip(s1, s2))
print("\n", s3)
for x, y in zip(s1, s2[::-1]):
    print(x, y)
name = {"Daquavis", "Technoblade"}
age = {21, 43}
s4 = dict(zip(name, age))
print(s4)