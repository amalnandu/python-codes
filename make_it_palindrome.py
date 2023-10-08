str=input()

left=0
right=len(str)-1
s=''

while(left<right):
    if(str[left]!=str[right]):
        s=str[left]+s
        left=left+1
    else:
        left=left+1
        right=right-1    


print(s)