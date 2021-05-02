# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the
# largest sum and return its sum.
# kadanes algorithm - dynamic programming


# def maxSubArray(self, nums: List[int]) -> int:
#         current_subarray = max_subarray = nums[0]
#         for num in nums[1:]:
#              current_subarray = max(num, current_subarray + num)
#              max_subarray = max(max_subarray, current_subarray)
#          return max_subarray


# leetcode :21. Merge Two Sorted Lists
# Python3 code to demonstrate
# to combine two sorted list
# using naive method

# initializing lists
test_list1 = [1, 5, 6, 9, 11]
test_list2 = [3, 4, 7, 8, 10]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# using naive method
# to combine two sorted lists
size_1 = len(test_list1)
size_2 = len(test_list2)

res = []
i, j = 0, 0

while i < size_1 and j < size_2:
    if test_list1[i] < test_list2[j]:
        res.append(test_list1[i])
        i += 1

    else:
        res.append(test_list2[j])
        j += 1

# res = res + test_list1[i:] + test_list2[j:]

# printing result
print("The combined sorted list is : " + str(res))


# iven a string num which represents an integer, return true if num is a strobogrammatic number.
# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
# method 1
def isStrobogrammatic(num) -> bool:
    ans = ""
    for m in num:
        if m == "6":
            ans = "9" + ans
        elif m == "9":
            ans = "6" + ans
        elif m == "8":
            ans = "8" + ans
        elif m == "1":
            ans = "1" + ans
        elif m == "0":
            ans = "0" + ans
        else:
            ans = ans + ""
    # print(ans)
    return ans == num


print(isStrobogrammatic("789"))


# method 2 using hashmap
def isStrobogramm(num):
    """
        :type num: str
        :rtype: bool
        """
    d = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    ans = ''
    for n in num:
        if n in d:
            ans += d[n]
        else:
            return False
        ans += d[n]
    return ans[::-1] == num


print(isStrobogramm('111'))


# an in-place algorithm.
# time complexity : o (n)
# space complexity : o(1)
def isStrobogrammatichashmap(num) -> bool:
    rotated_digits = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}

    left = 0
    right = len(num) - 1

    while left <= right:
        if num[left] not in rotated_digits \
                or num[right] != rotated_digits[num[left]]:
            return False
        left += 1
        right -= 1
    return True


print("THE VALUE 111 is = ", isStrobogrammatichashmap("111"))

# x = 3
# nums = x % 2 * list('018') or ['']
# print (nums)

#20.valid parenthesis

def isValid(s: str) -> bool:
    if s == 0 or len(s) == 0:
        return True

    stack = []
    for char in s:
        if char == '(' or char == '{' or char == '[':
            stack.append(char)
        elif char == ")" and (len(stack) == 0 or stack[-1] != "("):
            return False
        elif char == "}" and (len(stack) == 0 or stack[-1] != "{"):
            return False
        elif char == "]" and (len(stack) == 0 or stack[-1] != "["):
            return False
        else:
            stack.pop()

    if len(stack) > 0:
        return False
    else:
        return True

