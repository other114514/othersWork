t=0
for i in range  (1,11):
    f=0
    for j in range(2,i+1):
        if not i%j and not 10%j: 
            f=1
            break
        else:
            pass
    if f==0:
        t+=1
        print(i)
print("TOTAL:",t)
