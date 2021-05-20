
# List and Tuple servers the same purpose but tuple  are immutable and list are not.
# Like we seen that we can change the elements in list but it wont b e possible in tuple

# So how would python understand that we want to deal with list not tuple?
# Simple for list we would specify square brackets and tuple the parenthesis

values = (1, 2, 3)
value = ("one", "three", "two", "four")
vlue =(1.3, 4.5, 6.3)

print(values[2])
print(value[1])
print(vlue[0])

print(values[-1])
print(value[-1])
print(vlue[-1])

print(values[0:2])

#values.insert(3, 6)
#print(values)

#values.append(100)
#print(values)

#values[1] = 5
#print(values)

#del values[0]
#print(values)