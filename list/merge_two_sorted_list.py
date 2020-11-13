
#Given two sorted lists, merge them into one list which should also be sorted
# Problem Statement #
#
# Implement a function that merges two sorted lists of m and n elements respectively, into another sorted list. Name it merge_lists(lst1, lst2).
# Input #
#
# Two sorted lists.
# Output #
#
# A merged and sorted list consisting of all elements of both input lists.

def merge_list(l1,l2):
    pt1 = 0
    pt2 = 0

    #traversing through the entire list
    while pt1 < len(l1) and pt2 < len(l2):

        #if first value is greater than second then insert before first
        if l1[pt1] > l2[pt2]:
            l1.insert(pt1,l2[pt2])
            pt1 += 1
            pt2 += 1

        # if both values are same, then only one element is required
        elif l1[pt1] == l2[pt2]:
            pt2 += 1

        # if the value is smaller than second, increment the counter to 1 so it will start comparing the second element to first
        else:
            pt1 += 1

    # if second counter is less than len of the second list
    if pt2 < len(l2):
        l1 = l1 + l2[pt2:]

    return l1


print(merge_list([1,3,4,5], [1,3,4,5,6]))
