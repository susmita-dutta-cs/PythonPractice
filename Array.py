
##rolling Sum of 1d array
# def sum_list(items):
#     a= 0
#     list =[]
#     for x in items:
#         a = x + a
#         list.append(a)
#     return list
# print("Rolling array sum 1d array :" ,sum_list([1,2,3,4]))


# define a new integer = 0
# create a new list
# return the list

# if we want the total sum of the array/ list = return a
# CANDIES:

# def kidwitcandies(values,extra):
#     ll=[]
#     for x in values:
#         if x + extra >= max(values):
#             ll.append(True)
#         else:
#             ll.append(False)
#     return ll
# print(kidwithcandies([2,3,5,1,5],2))


# make a new list
# for every element in the 1st list , if every element + extra candy are added and it is greater than or equal to the highest number in the first list ,
# it will append true in the new list else it will be false

# def maxwealth(accounts):
#     num= 0
#     # ll =[]
#     for i in accounts:
#         for j in i:
#             num = num +j
#         # ll.append(num)
#     return num
# print(maxwealth([[1,5],[7,3],[3,5]]))
# #summation of all the values in a nested list

def maxwealth(accounts):
    # num= 0
    ll = []
    # new list
    for i in accounts:
        # for every nested list in the original list
        ll.append(sum(i))
        # add the sum of the elements in the new list ll

    return max(ll)


print(maxwealth([[1, 5], [7, 3], [3, 5]]))


def shuffle(nums,n):
    # Create An Empty Array To Store Results
    arr = []

    # Iterate Through First Half Of The Array(lenght of array divided by 2 or simply n)
    for i in range(n):
        # Add The ith element and the (n + i)th element as mentioned in problem
        arr.extend([nums[i], nums[n + i]])
    # Return array
    return arr


print(shuffle([2, 3, 4, 1], 2))

