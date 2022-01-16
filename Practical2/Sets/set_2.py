#20cs027 shubhang khemani
#defining function to remove items
def removeitem(set,item):
    set.discard(item)
    return set
set = {1,2,3,4,5,6,7}
#calling function
set = removeitem(set,2)
#printing results
print(set)
#calling function
set = removeitem(set,10)
#printing results
print(set)