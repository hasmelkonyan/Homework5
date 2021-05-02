# 1. Implement bubble sort(do some research) algorithm

def bubble_sort(lst=[]):
    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = [lst[j + 1], lst[j]]
    return lst


print(bubble_sort([8, 2, -1, 14, 0]))


# 2. Concatenate two lists index-wise.
# Input:
#
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# Output:
#
# ['My', 'name', 'is', 'Kelly']

def mix_lists(lst1=[], lst2=[]):
    if len(lst1) == len(lst2):
        for i in range(0, len(lst1), 1):
            print(lst1[i] + lst2[i], end=' ')
    else:
        print("The number of members on your list isn't equal")


mix_lists(["M", "na", "i", "Ke"], ["y", "me", "s", "lly"])


# 3.Given a Python list of numbers. Turn every item of a list into its square

def each_item_to_its_square(lst=[]):
    new_lst = []
    for each in lst:
        each = each ** 2
        new_lst.append(each)
    return new_lst


print(each_item_to_its_square([1, 4, 8, 0, 5]))


# 4. Write a program that will calculate sum of lists members.

def sum_of_lists_members(lst=[]):
    sum = 0
    for each in lst:
        sum += each
    return sum


print(sum_of_lists_members([8, 4, 5, -8, 7]))


# 5. Write a Python program to remove duplicates from a list.

def remove_duplicates(lst=[]):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst


print(remove_duplicates([0, 8, 0, 9, 10, 0, 8, 10, 0]))


# 6. Write a Python program to get unique values from a list.

def unique_values(lst=[]):
    new_lst = []
    for i in lst:
        if lst.count(i) == 1:
            new_lst.append(i)
    return new_lst


print(unique_values([1, 4, 4, 10, 1, 8, 0, 9]))
