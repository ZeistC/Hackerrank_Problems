def Mod_kap(n):
    d = len(str(n))
    if n==1:
        return(True)
    if n in [i for i in range(2,9)]:
        return(False)
    if len(str(n*n))==2*d or len(str(n*n))==(2*d)-1:
        r = int(str(n*n)[-d::])
        l = int(str(n*n)[:-d])
    if l+r==n:
        return(True)
    else:
        return(False)
def kaprekarNumbers(p, q):
    kap = []
    for i in range(p,q):
        if(Mod_kap(i)):
            kap.append(i)
    if len(kap)==0:
        print("INVALID RANGE")
    else:
        for i in kap:
            print(i,end=" ")
    

if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)