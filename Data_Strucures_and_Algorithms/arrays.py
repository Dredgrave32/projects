new_list = [1, 2, 3]
result = new_list[0]
#works in Constant Time and crashes when accessing an outof bounds index

if 1 in new_list: print(True) #inline python if statement

print("New list contatins: ", new_list)
print("Result at index 0: ", result)

for n in new_list:
    if n ==1:
        print(True)
        
        break
    
# True insert is a index value and has a linear runtime
# Appending is a Constat time operation and appends the value to the end of a list

numbers = []
print(numbers)
print(len(numbers))
numbers.append(2) #updates the memeory allocation to 1
print(numbers)
print(len(numbers))
numbers.append(200) #Increases the memory allocation with a memopry re-size operation
print(numbers)
print(len(numbers))

numbers.extend([4,5,6])
print(numbers)
print(len(numbers))