str=input("Enter your string ")
hash_count=0

for i in range(len(str)):
    if str[i]=='#':
        hash_count=hash_count+1


str2=''
for i in str:
    if i !='#':
        str2=str2+i


for i in range(hash_count):
    str2='#'+str2  

print(str2)          