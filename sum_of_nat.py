# approach 1
""" def fun(n):
    return n*(n+1)/2
print("sum of natural numbers", fun(5))  """
def fun1(n):
    sum=0
    for i in range(1,n+1):
        sum = sum + i
    return sum
print("sum  is ", fun1(5))