def threeNPlusOne (i, j, n=-1, r=0):
    if n == -1:
        n = j
    
    if n == 1:
        return r

    if n % 2 != 0:
        n = 3 * n + 1
    else:
        n = n / 2
    return threeNPlusOne(i,j,n,r+1)



    
    
