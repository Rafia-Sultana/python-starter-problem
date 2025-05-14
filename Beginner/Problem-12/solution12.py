list1 = [3, 5, 7, 4, 8, 8]
list2 = [4, 9, 8, 7, 1, 1, 13]

common_items = []

for item in list1:
    if item in list2 and item not in common_items:
        common_items.append(item)

total = sum(common_items)
print("Common items:" , common_items)
print("Sum of common items", total)
