from itertools import count


arr = [3,3,2,1,3]
large = 0
num = 0
for i in arr:
    c = arr.count(i)
    if c>large:
        large = c
        num = i
d = 0 
for i in arr:
    if i!=num:
        d+=1
print(d)
    
        
        