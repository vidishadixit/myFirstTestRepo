#like numeric data types for arrays also we need not to specify type for creating

values = [1, 2, 3, 4]

value = [2.4, 5.6, 8.9, 44.5]

vlue = ["one", "three", "two", "four"]

print(values[3])
print(value[0])
print(vlue[2])

# in python there is one syntax that will allow to print last element in array using below

print(values[-1])
print(value[-1])
print(vlue[-1])

# if we want to serially print numbers in array use below syntax, Last index is exclusive

print(values[0:3])

# if we want to insert any element at any index we can do so by below command

values.insert(3, 6)
print(values)

#if we want to add any element at the last index below is the command

values.append(100)
print(values)

# if we want to change values of any element use below command

values[1] = 5
print(values)

#if you want to delete any of the element you can use below command

del values[0]
print(values)