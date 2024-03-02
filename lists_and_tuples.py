# There are four collection data types in the Python programming language:
#
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# List items are ordered, changeable, and allow duplicate values.
# List items can be of any data type:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]
print(list1)
print(f'length: {len(list1)}, type: {type(list1)}')

list4.append("female")
for x in list4:
    print(x)

for i in range(len(list1)):
    print(list1[i])

list1.remove("banana")
[print(x) for x in list1]

# Tuples are used to store multiple items in a single variable.
# Tuple items are ordered, unchangeable, and allow duplicate values.
thistle = ("apple", "banana", "cherry")
print(thistle)

x = [[4, 0, 1], [0, 0, 1], [0, 1, 2], [1, 1, 0], [2, 0, 0]]
print(f"x length: {len(x)}")
print(x[0][0])
