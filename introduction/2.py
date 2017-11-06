name = str(input("Please enter a four character string: "))

n1 = chr(ord(name[0]) - 32)
n2 = chr(ord(name[1]) - 32)
n3 = chr(ord(name[2]) - 32)
n4 = chr(ord(name[3]) - 32)
name_cap = n1 + n2 + n3 + n4
if len(name) > 4:
    print('The string capitalized is %s'%(name_cap+name[4:]))
else:
    print('The string capitalized is %s'%(name_cap))

