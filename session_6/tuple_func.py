item=('Doney',22,'Kottayam')
item_list=list(item)
item=tuple(item_list)
#how to assign each values

#Method 1:
name,age,place=item
print(f"{name},{age},{place}")

#Method 2:
names=item[0]
places=item[2]
print(names,places)