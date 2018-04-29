def n_times():
     n=input("enter an integer: ")
     def helper(k):
         if k!=0:
              print(n)
              return helper(k-1)
         else:
              return None
     return helper(int(n))

print(n_times())
