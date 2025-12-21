list1 = [1, 2, 3, 4, 5, 4, 3, 2, 2]

copy_list1 = list1.copy()
copy_list1.reverse()

if (copy_list1 == list1):
    print("list1 is palindrome")

else:
    print("list is not a palindrome")