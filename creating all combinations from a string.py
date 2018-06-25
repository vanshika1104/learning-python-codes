import itertools
word=input("Enter the word\n")
l=[]
l=word
count=0
combinations=1;
for i in range(1,len(word)+1):
    combinations*=i
print("No. of combinations:",combinations)
for m in itertools.permutations(l,len(l)):
    output=''
    count+=1
    for x in m:
        output+=x
    print("Combination #",end='')
    print(count,":",output)
        
        
    
