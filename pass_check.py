def pass_check():
     x = input("What is the password? : ")
     if (check1(x) and check2(x) and check3(x) and check4(x)):
         print("Thank You")
         return x
     else:
         print("Invalid password")
         return pass_check()


def check1(s):
     if len(s)==0:
          return True
     else:
          return (s[0:1].isupper()) or check1(s[1:])

def check2(s):
     if len(s)==0:
          return False
     else:
          return (s[0:1].islower()) or check2(s[1:])

def check3(s):
     if len(s)==0:
          return False
     else:
          return (s[0:1].isnumeric()) or check3(s[1:])
def check4(s):
     if len(s)==0:
          return True
     else:
          return (not (s[0:1].isspace())) and check4(s[1:])

##pass_check()
