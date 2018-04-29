def str_score (s) :
    if len(s)==0:
         return 0
    elif s[0:1].isalpha():
         return 1 + str_score(s[1:])
    elif s[0:1].isdigit():
         return int(s[0:1])+str_score(s[1:])
    else:
         return str_score(s[1:])


print(str_score("CS 116"))
