#20cs027 shubhang khemani
#d. Write a Python script to add a key to a dictionary.
def addkey(dict,keyname,keyvalue):
    dict[keyname] = keyvalue
    return dict

dict = {0: 10, 1: 20}
keyname = 2
keyvalue = 30

dict = addkey(dict,keyname,keyvalue)

print(dict)