arr = [5,4,4,2,2,8]
while(len(arr)>0):
        count = 0
        i=0
        while(i<len(arr)):
            if arr[i]==0:
                arr.remove(arr[i])
                i-=1
            i+=1
        if len(arr)==0:
            break
        m = min(arr)
        for i in range(len(arr)):
            arr[i] = arr[i]-m
            count+=1
            
        print(count)