def gcd(a,b):
    while a != b:
        if a > b:
            a=a-b
        else:
            b = b-a
    return a
a=5
b=7
print(gcd(a,b))