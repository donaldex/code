import math
def is_prime(n):
     def mod_check(p,N):
          if p==N:
               return True
          elif p%N==0:
               return False
          else:
               return True and mod_check(p,N+1)
     return mod_check(n,2)

print(is_prime(2))
print(is_prime(5))
print(is_prime(6))
print(is_prime(7))
print(is_prime(8))
print(is_prime(9))


