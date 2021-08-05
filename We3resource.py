# 68.Write a Python program to extend a list without append.


# y[:0] = x
# def insert(list, n):
#     # searching for position
#     for i in range(len(list)):
#         if list[i] > n:
#             index = i
#             break
#
#     value = list[:i] + [n] + list[i:]
#     return value
#
#
# list = [10, 20, 30]
# n = 43
#
#
# # print(insert(list, n))
#
#
# # insertion sort algorithm
# # unsorted sequence
#
# def insertionsort(list_a):
#     indexing_length = range(1, len(list_a))
#     for i in indexing_length:  # for every value
#         value_to_sort = list_a[i]  # one by one element of indexing length
#         while list_a[i - 1] > value_to_sort and i > 0:  # value on the left is larger
#             # than right value we need to swap it and i >0 because python allows negative index
#             list_a[i], list_a[i - 1] = list_a[i - 1], list_a[i]
#             i = i - 1  # incrementally stepping of the i variable
#     return list_a
#
#
# print("the sorted list is = ", insertionsort([3, 7, 9, 6, 5]))
#
#
# # summing all the elements in a list
# def sum_list(items):
#     total = 0
#     for i in items:
#         total += i
#     return total
#
#
# print("the total sum of all the elements is ", sum_list([1, 2, 3, 4, 5]))
#
#
# def merge(a, b):
#     """
# 	a and b are two sorted lists
# 	"""
#     i = 0  # pointer
#     j = 0  # 2nd list pointer
#     c = []
#     while i < len(a) and j < len(b):  # if both of them are non empty
#         if a[i] < b[j]:  # if the value of list 1 is less then value of list 2
#             c.append(a[i])  # add to the new list
#             i += 1
#         else:
#             c.append(b[j])  # if its opposite l2 > l1 value
#             j += 1
#     if i < len(a):  # what if one of them is empty then this portion will work
#         while i < len(a):
#             c.append(a[i])
#             i += 1
#     if j < len(b):
#         while j < len(b):
#             c.append(b[j])
#             j += 1
#     return c
#
#
# a = [1, 5, 6, 9]
# b = [2, 4, 8]
# print(merge(a, b))
#
# L = [1, 2, 2, 1]
#
#
# def sum(items):
#     total = 1
#     for i in items:
#         total = total * i
#     return total
#
#
# print(sum(L))


def common_elements(list1, list2):
    result = []
    for element in list1:
        if element in list2:
            result.append(element)
    return result


a1 = [2, 4, 0, 7, 9]
b1 = [7, 8, 9, 1]
print("common = ", common_elements(a1, b1))


def uncommon_elements(list1, list2):
    res_list = []
    for i in list1:
        if i not in list2:
            res_list.append(i)
    for i in list2:
        if i not in list1:
            res_list.append(i)
            return res_list


print("The uncommon of two lists is : ", uncommon_elements(a1, b1))

# initializing list
test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print("The original list is : " + str(test_list))


# using naive method
# to remove duplicated
# from list
# def dup(ll): # removing duplicate elements a
#     res_list = []
#     for i in ll:
#         if i not in res_list:
#             res_list.append(i)
#             i+=1
#     return res_list
#
#
# # printing list after removal
# print("The list after removing duplicates : ", dup(test_list))


def migratoryBirds(arr):
    typecount = [0] * len(arr)
    for i in arr:
        typecount[i] += 1  # because in python array starts from 0
    max_count = max(typecount)
    for i in range(len(arr)):
        if typecount[i] == max_count:
            return i


arr = [1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 2, 2, 2]
print("value ", migratoryBirds(arr))


# dictionary

# reverse a list
def reverse_in_place(lst):  # Declare a function
    size = len(lst)  # Get the length of the sequence
    hiindex = size - 1
    its = int(size / 2)  # Number of iterations required
    for i in range(0, its):  # i is the low index pointer
        temp = lst[hiindex]  # Perform a classic swap
        lst[hiindex] = lst[i]
        lst[i] = temp
        hiindex -= 1  # Decrement the high index pointer
    return lst


# Now test it!!
array = [2, 5, 8, 9, 12, 19, 25, 27, 32, 60, 65, 1, 24, 124, 654]

# print (array)                 # Print the original sequence
print(reverse_in_place(array))  # Call the function passing the list


def transposematrix(A): # declare  a fuction
    numrows, numcols = len(A), len(A[0]) # get the length of the rows and columns
    newgrid = []  # create another matrix wth the new dimensions because of flipping
    for z in range(numcols):
        newgrid.append([0] * numrows)

    for r in range(numcols): # looping over the columns
        for c in range(numrows):
            newgrid[r][c] = A[c][r] # assign the values on the new matrix by flipping indexes
    return newgrid # return new matrix


matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(transposematrix(matrix))

