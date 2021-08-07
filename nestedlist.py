# 2-D List
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

flatten_matrix = []

for sublist in matrix:
    for val in sublist:
        flatten_matrix.append(val)

print(flatten_matrix)

# 2-D List of planets
planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']]

flatten_planets = []

for sublist in planets:
    for planet in sublist:

        if len(planet) < 6:
            flatten_planets.append(planet)

print(flatten_planets)


# Here we have used the technique of Bubble Sort to perform the sorting.
# We have tried to access the second element of the sublists using the nested loops.
# This performs the in-place method of sorting. The time complexity is
# similar to the Bubble Sort i.e., O(n^2)
# Python code to sort the lists using the second element of sublists
# Inplace way to sort, use of third variable
def Sort(sub_li):
    l = len(sub_li)
    for i in range(0, l):
        for j in range(0, l - i - 1):
            if (sub_li[j][1] > sub_li[j + 1][1]):
                tempo = sub_li[j]
                sub_li[j] = sub_li[j + 1]
                sub_li[j + 1] = tempo
    return sub_li


# Driver Code
sub_li = [['rishav', 10], ['akash', 5], ['ram', 20], ['gaurav', 15]]
print(Sort(sub_li))


# Python3 code to demonstrate working of
# Check for Sublist in List
# Using loop + list slicing

# initializing list


# Check for Sublist in List
# Using loop + list slicing
def valuecheck(test_list, sublist):
    for i in range(len(test_list) - len(sublist) + 1):
        if test_list[i: i + len(sublist)] != sublist:
            return True


# printing result
test_list = [5, 6, 3, 8, 2, 1, 7, 1]

# printing original list
# initializing sublist
sublist = [8, 2, 1]
print(valuecheck(test_list, sublist))
