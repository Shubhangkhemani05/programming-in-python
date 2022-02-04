x = int(input())
lst = list(map(int, input().split()))
var1 = set()
var2 = set()
for room in lst:
    if room not in var1:
        var1.add(room)
        var2.add(room)
    else:
        var2.discard(room)

var2 = list(var2)
print(var2)
