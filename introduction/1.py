name = str(input("Please Enter your name: "))
print(name[0] + ' ' + 'ASCII value is ' + str(ord(name[0])))

for c in range(4):
    print("%s ASCII value is %d"%(name[c],ord(name[c])))
