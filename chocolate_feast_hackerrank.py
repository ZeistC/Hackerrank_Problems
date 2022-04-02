n = 6
c = 2
m = 2


c_bars = n//c   
tot_bars = c_bars
if c_bars<m:
    print(c_bars)
    #break
    
while(c_bars>=m):
    bars = c_bars//m     
    tot_bars+=bars      
    c_bars = bars+(c_bars-(m*bars))  
print(tot_bars)