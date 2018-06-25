print("Enter your choice")
c=input("Do you want to add or delete triangles: ")
'''
code to alter the data of triangles file
'''
if (c in ('add','del','delete','+','-','ADD','DELETE','DEL')):
    choice=int(input("Enter the no. of triangle you want to add/delete more: "))
'''
code to add more triangles on choice
'''
if (c in('add','+','ADD')):
    import random as r
    file=open("triangles.txt","a")

    for i in range(choice):
        file.write("[")

        for x in range(1,4):
            file.write('[')

            for n in range(1,4):
                file.write("%i,"%(r.randint(-50,50)))

            file.write(']')

        file.write(']\n')

    file.close()
'''
code to delete triangles on choice
'''
if (c in ('del','delete','-','DEL','DELETE')):
    file=open("triangles.txt","r")
    b=file.readlines()
    file1=open("triangles.txt","w")
    for j in range((len(b)-choice)):
        file1.write(b[j])
    print("Last",choice,"triangles have been deleted")   
    file1.close()
    file.close()
'''
code to interpret and manipulate data for results
'''
file=open("triangles.txt","r")
b=file.readlines()
s=[]
total=0
area=0

for i in range (len(b)):
    d=[]
    a=b[i].split('[')
    
    for n in range (len(a)):
            c=[]
            
            if(a[n]!=''):
                c=(a[n].split(',]'))
                e=c[0].split(',')
                
                for m in range (len(e)):
                    e[m]=int(e[m])
                
                d.append(e)
                
    s.append(d)
    
for x in range(len(s)):
        area=((s[x][0][0]*(s[x][1][1]*s[x][2][2]-s[x][1][2]*s[x][2][1]))-(s[x][0][1]*(s[x][1][0]*s[x][2][2]
              -s[x][1][2]*s[x][2][0]))+(s[x][0][2]*(s[x][1][0]*s[x][2][1]-s[x][1][1]*s[x][2][0])))
        area=abs(0.5*area)
        #print("Area of triangle",x+1,"is:",area) #remove first '#' if you want to print the area of each triangle as well
        total+=area
'''
code to display no. of triangles and sum of their areas
'''
print("no. of triangles:",len(b))        
print("Sum of areas of all triangles is:",total,"sq units")
file.close()
