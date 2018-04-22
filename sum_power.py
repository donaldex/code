import math
def sum_power(b,n):
     if n==0:
          return 1
     else:
          return b**n+sum_power(b,n-1)
print(sum_power(5,2))
