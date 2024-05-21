l=[0,0,0]
iii=0
def f(n):
    global l,iii
    if n==0:
        if not 0 in l:print(l)
        l=[0,0,0]
        return
    for i in range(1,4):
        if i not in l:
            l[n-1]=i
            f(n-1)
        else:continue
f(3)
