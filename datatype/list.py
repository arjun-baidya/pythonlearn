# A list in Python is used to store the sequence of various types of data
#Python lists are mutable type its mean we can modify its element after it created
# A list can be defined as a collection of values or items of different types. The items in the list are separated with the comma (,) and enclosed with the square brackets [].

# Characteristics of Lists
# The lists are ordered.
# The element of the list can access by index.
# The lists are the mutable type.
# The lists are mutable types.
# A list can store the number of various elements.
########################################################################################################################
# difference between remove,pop and del

# ## Del
# del basically works on the index.
# in Python, del is a keyword.

# remove()
# Remove basically works on the value.
# In Python, remove() is an in-built method.

# pop()
# pop basically works on the index.
# In Python, pop() is an in-built method.
########################################################################################################################
simpleList = ["red", "green", "blue", 4, 5, 6]
print(simpleList)
print(type(simpleList))

#simpleList[1] = green type is str 
print("simpleList[1] = ", simpleList[1])

print(type(simpleList[1]))

#simpleList[4] = 5 type is int 
print("simpleList[4] = ", simpleList[4])

print(type(simpleList[4]))

# simpleList[0:3] = ['red', 'green']
print("simpleList[0:3] = ", simpleList[0:3])

# simpleList[3:] = [4, 5, 6]
print("simpleList[3:] = ", simpleList[3:])

# chagig value of item in list
simpleList[2] = 3
print("value did changed", simpleList)

# get last value of list
print("simpleList[-1] = ", simpleList[-1])

#we can add value to list
simpleList.insert( 6,"new value")
print("New item added to list",simpleList)

#we can remove value from list by item value
simpleList.remove( "new value")
print("one item removed from list by value",simpleList)

#we can remove value from list by item index
simpleList.pop(2)
print("one item removed from list by index", simpleList)

#we can run for loop on list
for x in simpleList:
  print(x)
