def quicksort(l,r):
    if l>r:
        return
    i,j=l,r
    base=a[l]
    v=1
    print('-')
    #别将两个过程扔到一个循环里！！三while不多说了
    #如非必要，莫添变量
    while i!=j:
        while a[j]>=base and i<j:
            print(a[j],j)
            j-=1
        while a[i]<=base and i<j:
            print(a[i],i)
            i+=1
        if i<j:
            a[j],a[i]=a[i],a[j]
    a[l],a[i]=a[i],a[l]
    quicksort(l,i-1)
    quicksort(i+1,r)
a=[114,54,3,1999,5]
print(a)
quicksort(0,4)
print(a)


            

