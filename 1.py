li=[0,3,4,9]
n=9
def f(l,r):
    mid=(l+r)//2
    if r<l:
        return -1;
    if li[mid]==n:
        return mid
    else:
        if li[mid]>n:
            return f(l,mid-1)
        else:
            return f(mid+1,r)
result=f(0,3)
print(result)
