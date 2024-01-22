arr = []
for i in range(5):
   name = input("Enter a name: ")
   number = int(input("Enter a number: "))
   arr.append([name, number])

dictionary = {}
for i in range(len(arr)):
   dictionary[arr[i][0]] = arr[i][1]

arr.sort(key=lambda x: x[1])

print("Sorted dictionary based on value:")
for key, value in dictionary.items():
   print(key, ":", value)
