word = input("Enter a word: ")
print("ORIGINAL:",word)
output=''
for x in range(0, len(word)):
    if(x%2==0):
        output+=word[x].upper()
    else:
        output+=word[x]
print("New value:",output)
