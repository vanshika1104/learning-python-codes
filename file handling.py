f=open("new.txt","a")
data=(input("Enter the data: "))

f.write(data)


f.close()
f1=open("new.txt",'r')
print(f1.read())
