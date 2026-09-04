lst = []

n = int(input("Enter number of elements: "))

for i in range(n):
    lst.append(input("Enter element: "))

print("Original List:", lst)

print("\nOccurrences:")
for item in set(lst):
    print(item, "->", lst.count(item))

lst.append("NEW")
print("\nappend():", lst)

lst.extend(["A", "B"])
print("extend():", lst)

lst.insert(1, "INSERTED")
print("insert():", lst)

print("index(NEW):", lst.index("NEW"))

lst.remove("NEW")
print("remove():", lst)

print("pop():", lst.pop())
print("After pop:", lst)

copied = lst.copy()
print("copy():", copied)

copied.reverse()
print("reverse():", copied)

temp = copied.copy()
temp.clear()
print("clear():", temp)

num = [10, 5, 20, 15]

print("\nNumeric List:", num)
print("len():", len(num))
print("max():", max(num))
print("min():", min(num))
print("sum():", sum(num))

num.sort()
print("sort():", num)

num.sort(reverse=True)
print("sort(reverse=True):", num)

print("sorted():", sorted(num))
