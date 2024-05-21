def f(i):
    if i>0:
        return i+f(i-1)
    else:
        return 0
print(f(10))
