b = 3
w = 5
bc = 3
wc = 4
z = 1

B_W = (b*bc)+(w*wc)
B = (b*bc)+((bc+z)*w)
W = ((wc+z)*b)+(w*wc)

print(min(B_W,B,W))

