# the following line reads the list from the input, do not modify it, please
old_list = [int(num) for num in input().split()]

binary_list = [0 if num < 1 else 1 for num in old_list] # your code here
print(binary_list)
