"""def gcd(a,b):
    while a != b:
        if a > b:
            a=a-b
        else:
            b = b-a
    return a
a=5
b=7
print(gcd(a,b)) """
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a % b)
a=9
b=15
print(gcd(a,b))