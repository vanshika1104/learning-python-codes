word=input()
output=''
count=0
for i in word:
    if(i!=' '):
        output+=i
    else:
        count+=1
print(output)
print("No. of spaces:",count)
