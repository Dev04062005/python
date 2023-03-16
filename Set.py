# Operation : 
"""
.update()
.remove()
.discart()
.union | 
.intersection &
.Difference
"""

Set = {1,2,34,4,2}
Set1 ={1,34,5,6,7,8}
print(Set)


# Union 
print(Set|Set1)

# Intersection 
print(Set & Set1)

# Difference
print(Set - Set1)

#update
Set.update(Set1)
print(Set)

#Add
Set.add(13)
print(Set)

# Discard Element from Tuple 
Set.discard(34)
print(Set)

# Remove
Set.remove(8)
print(Set) 

# Pop 
Set.pop()
print(Set)

#Copy 
print(Set.copy())

#Type Cast
tup =tuple(Set) 
print(tup)

