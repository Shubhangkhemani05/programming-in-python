#20cs027 shubhang khemani
#creating a tuple
shubhang = (7, 1, 0, 55, 33, 17)
print(shubhang)
#using merge of tuples with the + operator you can add an element and it will create a new tuple, because tuples are immutable
shubhang = shubhang + (94,)
print(shubhang)
#adding items in a specific index
shubhang= shubhang[:5] + (25, 2, 56) + shubhang[:5]
print(shubhang)
#converting the tuple to list
listx = list(shubhang)
#use different ways to add items in list
listx.append(30)
shubhang = tuple(listx)
print(shubhang)