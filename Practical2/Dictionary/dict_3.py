#20cs027 shubhang khemani
# c. Write a Python program to sum all the items in a dictionary.

# funtction to find the sum of all vales of all keys in a dictionary
def sumofdict(dict):
    sum = 0
    #for every key add the value to sum
    for key in dict.keys():
        sum += dict[key]
    return sum

#samle dictionary
dict = {'A': 1, 'B':2, 'C':3}

print(sumofdict(dict))