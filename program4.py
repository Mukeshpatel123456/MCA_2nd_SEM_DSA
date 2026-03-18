# One-dimentional array

arr =[]
n = int(input("Enter number of elements: "))

for i in range(n):
   element = int(input("Enter element: "))
   arr.append(element)

print("Array elements are here ->", arr)

for i in range(len(arr)):
    print("index",i,"=", arr[i])
