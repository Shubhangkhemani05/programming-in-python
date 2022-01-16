#20cs027 shubhang khemani
def concatenatedict(dicts):
    newdict = {}
    for dict in dicts:
        for key in dict.keys():
            newdict[key] = dict[key]
    return newdict

dic1={1:10, 2:20}

dic2={3:30, 4:40}

dic3={5:50,6:60}


newdict = concatenatedict([dic1,dic2,dic3])
print(newdict)