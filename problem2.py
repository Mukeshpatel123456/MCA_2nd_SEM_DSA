lst = [10,20,30,40,50]

print("list are here ->", lst)
# for inserting 

# pos = int(input("Enter the position of element you want to insert :"))
# element = int(input("Enter the element you want to insert :"))

# if pos>= 0 and pos<=len(lst):
#  lst.insert(pos,element)
#  print("Element inserted successfully ")
# else:
#   print("invalid poistion ")

# print("update list is here ->",lst)

#  for deleting 
# if pos>= 0 and pos<len(lst):
#     deleted_element = lst.pop(pos)
#     print("Element deleted successfully ", deleted_element)
# else:
#     print("invalid poistion ")

# print("update list is here ->",lst)


# for  searching

element = int(input("Enter the element you want to search :"))
if element in lst:
    print("Element found ->",lst.index(element) )
else:
    print("not found")