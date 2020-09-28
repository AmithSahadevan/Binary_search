position = -1

def search(lists, x):

	l = lists[0]
	u = len(lists)

	while l <= u:
		mid = (l+u)//2

		if lists[mid] == x:
			globals()["position"] = mid
			return True

		elif lists[mid] > x:
			u = mid - 1
		else:
			l = mid + 1
	return False

lists = [1,2,3,4,5,6,7,8,9,10,34,56,76,32,45,89,77,65,21,98,100,55,44,30]
lists.sort()
print("\n",lists)
x = int(input("\nEnter the number that you want to search: "))

if search(lists, x):
	print("Found at the position", position+1)
else:
	print("Not found")