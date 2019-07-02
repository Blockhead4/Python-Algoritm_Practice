def gcdlcm2(a, b):
    if a < b:
        a, b = b, a
    if a % b != 0:
        c = a % b
        while c:
            c , b = b % c, c   
    return(b)


]
    
a=15
b=24

print(gcdlcm(a, b))