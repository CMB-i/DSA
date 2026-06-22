#naive gcd
def naive_gcd(m,n):
    fm = []
    for i in range(1, m+1):
        if (m % i) == 0:
            fm.append(i)
    fn = []
    for j in range(1, n+1):
        if (n % j) == 0:
            fn.append(j)
    cf = []
    for f in fm:
        if f in fn:
            cf.append(f)
    return(cf[-1])

#gcd
def gcd(m,n):
    a = []
    b = max(m,n)
    for i in range(1, b+1):
        if (m % i) == 0:
            if (n % i) == 0:
                a.append(i)
    return(a[-1])

m = int(input("enter m: "))
n = int(input("enter n: "))
print (naive_gcd(m,n))
print (gcd(m,n))