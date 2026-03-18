list = [ ]
 
 #for adding element in list
list.append(10)
list.append(20)
list.append(30)
list.append(40)
list.append(50)

print("after append", list)

#Traversal

print("Traversal of list is here ->")
for i in list:
    print("After travarsal",i)

#Searching 

key = 20
 
if key in list:
    print("Element is here")
else:
    print("Element is no here ")

#Deletion
list.remove(20)
print("after deletion", list)

#lenght of the list

print("Length of the list is here ", len(list))