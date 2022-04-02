arr = [1,2,3,4,5]
d = 2
arr2 = []
for i in arr[d::]:
    arr2.append(i)
for j in arr[0:d]:
    arr2.append(j)
print(arr2)