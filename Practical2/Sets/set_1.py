#20cs027 shubhang khemani
#defining function to add items
def addtoset(set,items):
    for item in items:
        set.add(item)
    return set

set = {"1","2","3","4"}

items = ['a','b','c','d']
#calling function
set = addtoset(set,items)

#printing results
print(set)