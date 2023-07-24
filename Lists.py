
list_1 = ['A', 'B', 'C', 'D', 'W', 'X', 'Y', 'Z']
list_2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list_3 = [3, 9, 0, 22, 1000, 45, -6]
list_4 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

print("list_1 type: ", type(list_1))
print("list_1 contents: ", list_1)
print("\n")

print("General Index Dump:")
print("The letter stored at the 0th index is: ", list_1[0])
print("The letter stored at the 1st index is: ", list_1[1])
print("The letter stored at the 2nd index is: ", list_1[2])
print("The letter stored at the 3rd index is: ", list_1[3])
print("The letter stored at the 4th index is: ", list_1[4])
print("\n")

print("Negative Index Dump:")
print("The letter stored at the -1 index is: ", list_1[-1])
print("The letter stored at the -2 index is: ", list_1[-2])
print("The letter stored at the -3 index is: ", list_1[-3])
print("The letter stored at the -4 index is: ", list_1[-4])
print("The letter stored at the -5 index is: ", list_1[-5])
print("\n")

print("Slicing Lists:")
print("Elements starting from 0 index to the 4th index = list_1[0:5]: ", list_1[0:5])
print("Elements starting from 1 index to the 5th index = list_1[0:6]: ", list_1[0:6])
print("Elements starting from 4 index to last index = list_1[4:]: ", list_1[4:])
print("Elements starting from 1 index to last index = list_1[1:]: ", list_1[1:])
print("Elements starting from 0 index to 6 index = list_1[:7]: ", list_1[:7])
print("Elements starting from 0 index to last index = list_1[:]: ", list_1[:])
print("Every other element from index 0 = list_1[0::2]: ", list_1[0::2])
print("Every other element from index 1 = list_1[1:8:2]: ", list_1[1:8:2])
print("\n")

print("Reversing a List:")
print("Print list_1 - list_1[::1]", list_1[::1])
print("Print list_1 reversed - list_1[::-1]", list_1[::-1])
print("\n")

print("Updating List #1:")
print("list_1 contents: ", list_1)
print("Changes: list_1[0] = @ and list_1[3] = 9")
list_1[0] = '@'
list_1[3] = 9
print("list_1 contents: ", list_1)
print("\n")

print("Updating List #2 with Slice function:")
print("list_2 type: ", type(list_2))
print("list_2 contents: ", list_2)
print("Updating list_2 via Slice = list_2[0:4] = 'A', 'B', 'C', 'D'")
list_2[0:4] = 'A', 'B', 'C', 'D'
print("Updated list_2 contents: ", list_2)
print("\n")

print("Appending List #1:")
print("list_1 contents: ", list_1)
list_1.append('0')
list_1.append(-10)
list_1.append(True)
print("Updated list_1 contents: ", list_1)
print("\n")

print("Insert into List #1:")
print("list_1 contents: ", list_1)
list_1.insert(0,'J')
list_1.insert(3,-10)
list_1.insert(4,True)
print("Updated list_1 contents: ", list_1)
print("\n")

print("Extend List #1:")
print("list_1 contents: ", list_1)
list_1.extend([100, 200, 300])
print("Updated list_1 contents: ", list_1)
print("\n")

print("Remove the last element from List #1:")
print("list_1 contents: ", list_1)
list_1.pop()
print("Updated list_1 contents - list_1.pop() ", list_1)
print("\n")

print("Remove the @ element from List #1:")
print("list_1 contents: ", list_1)
list_1.remove('@')
print("Updated list_1 contents - list_1.remove('@') ", list_1)
print("\n")

print("Remove the first element from List #1:")
print("list_1 contents: ", list_1)
del list_1[0]
print("Updated list_1 contents - del list_1[0] ", list_1)
print("\n")

print("Maximum element from list_3")
maxValue = max(list_3)
print("max(list_3) =", maxValue)
print("\n")

print("Minimum element from list_3")
minValue = min(list_3)
print("min(list_3) =", minValue)
print("\n")

print("list_1 contents: ", list_1)
print("True element count - list_1.count(True)", list_1.count(True))
print("First True element - list_1.index(True)", list_1.index(True))
print("\n")

print("Reversing alternate method & sorting")
print("list_4 contents: ", list_4)
list_4.reverse()
print("list_4 - list_4.reverse(): ", list_4)
list_4.sort()
print("list_4 - list_4.sort(): ", list_4)
print("\n")



