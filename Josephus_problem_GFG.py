N = int(input())
k = int(input())
k-=1
arr = []
index = 0
for i in range(1,N+1):
    arr.append(i)
while len(arr)>0:
    if len(arr)==1:
        print(arr[0])
        break
    else:    
        index = (index+k)%len(arr)
        arr.pop(index)
