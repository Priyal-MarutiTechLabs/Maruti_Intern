set = {1,2,3,4,5,6}

print(set)

print("Number of elements present in set : {0}".format(len(set)))
print("Sum: {0}".format(sum(set)))

print("Sorted elements:")

print(sorted(set))

#add
set.add(8)
print(set)

#remove
set.remove(3)
print(set)

#set operations
set1 = { 'a', 'b', 'c', 'c', 'd' }
set2 = { 'a', 'b', 'x', 'y', 'z' }

print("Set 1:", set1)
print("Set 2:", set2)
print("intersection:", set1.intersection(set2))
print("union:", set1.union(set2))
print("difference:", set1.difference(set2))
print("symmetric difference:", set1.symmetric_difference(set2))

#Immutable sets (sets that cannot be modified) are created with the frozenset() function
s1 = frozenset(('blue', 'green', 'red'))
s1.add('brown')