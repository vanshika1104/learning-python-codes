import itertools
l=[]
choice='yes'
count=0

while (choice in ('yes','y','1','YES','Y')):
    element=input("Enter the element of list: ")
    l.append(element)
    choice=input("Do you want to enter more elements?\n")

for m in itertools.permutations(l,len(l)):
    count+=1
    print(m)
print (count)
