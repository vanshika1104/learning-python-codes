import itertools
l=[]
choice='yes'

while (choice in ('yes','y','1','YES','Y')):
    element=input("Enter the element of list: ")
    l.append(element)
    choice=input("Do you want to enter more elements?\n")
    
for i in range(len(l)+1):
    for a in itertools.combinations(l, i):
        print(a)

