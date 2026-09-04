n = int(input("Enter list size: "))

lst = []

for i in range(n):
    lst.append(input("Enter element: "))

print("\nList:", lst)

print("\nOccurrences of all elements:")
for item in set(lst):
    print(item, "->", lst.count(item))

ele = input("\nEnter element to delete: ")

while ele in lst:
    lst.remove(ele)

print("List after deletion:", lst)
