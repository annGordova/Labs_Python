#4, 16, 28, 40, 52





def f28(a):
    mx = max(a)
    mn = min(a)
    imx = a.index(mx)
    imn = a.index(mn)
    if imn > imx:
        return a[imx+1:imn]
    else:
        return a[imn+1:imx]



