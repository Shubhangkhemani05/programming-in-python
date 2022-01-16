#20cs027 shubhang khemani
#  b. Write a Python script to merge two Python dictionaries.



# sample dictionaries
d1 = {'a': 100, 'b': 200}
d2 = {'c': 300, 'd': 400}
#making a copy of d1
d = d1.copy()
#adding d2 to d
d.update(d2)
#printing d
print(d)