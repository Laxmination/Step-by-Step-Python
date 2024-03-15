tup =(1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 200, 300, 81, 28, 500, 81)

x =81

indx =0
while indx < len(tup):
    if(tup[indx] ==x):
        print("Found at index ", indx)
    else:
        print("Loading....")
    indx +=1
    