####

# Problem Statement  :

# You’re given a string where multiple characters are repeated consecutively. You’re supposed to reduce the size of this string using mathematical logic given as in the example below :

# Input :
# aabbbbeeeeffggg

# Output:
# a2b4e4f2g3

# Input :
# abbccccc

# Output:
# ab2c5


####

str=input()
i=1
c=1
l=[]
while(i<len(str)):
    if str[i]==str[i-1]:
        c=c+1
    else:
        print(str[i-1],end="")    
        print(c,end="")
        c=1
    i=i+1

print(str[i-1],end="")
print(c)
