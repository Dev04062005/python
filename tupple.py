tup1 = (2,3,4,"hi")
tup = (23,45,76,33,33)
print(tup)

# Slicing : 
print(tup[1:3])
print(tup[0:])
print(tup[ :3])
print(tup[-3 : ])

#Len :
print(len(tup))

# Empty Tuple
Etup =()
Otup = (50,)
print(type(Etup))
print(Etup)
print(type(Otup))
print(Otup)

# Tuple Mehtods : 
print(tup[4])
print(sum(tup))
print(tup.count(33))


# Concate Tuple :
Ctup = tup+Otup
print(Ctup)

#Type cast to list : 
li=list(tup)
print(li)

# Deleting Tuple :
del Otup
# print(Otup) //Error 

# Clear
