import math
n=6
f=1
print(math.factorial(n))#done by importing math function
for i in range(n,n+1):#done by iteration
   f*=i
   print(f)
def fact(n):#done by recursive function
   return if n<=1 else n*fact(n-1)
print(fact(6))

