import random
s=[]
size=0
area=0
total=0
choice='y'
while(choice=='y' or choice=='Y'or choice=="yes"or choice=="YES"or choice=='1'):
    t=[]
    for i in range(3):
        c=[]
        for j in range(3):
            data=random.randint(-50,50)
            c.append(data)
        t.append(c)
    area=((t[0][0]*(t[1][1]*t[2][2]-t[1][2]*t[2][1]))-(t[0][1]*(t[1][0]*t[2][2]-t[1][2]*t[2][0]))+(t[0][2]*(t[1][0]*t[2][1]-t[1][1]*t[2][0])))
    if (area!=0):
        s.append(t)
    choice=input("Do yo want to create one more triangle: ")  
print("No. of triangles created are:",len(s))
for x in range(len(s)):
        area=((s[x][0][0]*(s[x][1][1]*s[x][2][2]-s[x][1][2]*s[x][2][1]))-(s[x][0][1]*(s[x][1][0]*s[x][2][2]-s[x][1][2]*s[x][2][0]))+(s[x][0][2]*(s[x][1][0]*s[x][2][1]-s[x][1][1]*s[x][2][0])))
        area=abs(0.5*area)
        #print("Area of triangle",x+1,"is:",area)
        total+=area

print("Sum of areas of all triangles is:",total,"sq units")
