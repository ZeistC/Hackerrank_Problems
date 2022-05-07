N = int(input())
arr = [int(i) for i in input().split()]
num = arr[0]
arr.pop(0)
k = int(input())
arr2 = []
arr2.append(num)
for i in arr[-k::]:
    arr2.append(i)
for i in arr[0:len(arr)-k]:
    arr2.append(i)
    
print(arr2)
