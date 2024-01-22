def format_names(names):
   formatted_names = []
   for name in names:
       name = name.replace(" ", "")
       name = name[0].upper() + name[1:].lower()
       name = name[:-2]
       formatted_names.append(name)
   formatted_names.sort()
   return formatted_names


names = []
for i in range(5):
   name = input("Enter a name: ")
   names.append(name)


formatted_list = format_names(names)


for index, name in enumerate(formatted_list, start=1):
   print(f"{index}. {name}")
