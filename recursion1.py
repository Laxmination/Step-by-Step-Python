def fac(i):
    if(i ==0 or i ==1):
        return 1
    else:
        return i *fac(i-1)


print(fac(6))
