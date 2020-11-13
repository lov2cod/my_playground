

#Remove even from list

def remove_even(list_of_numbers):
    odd = []
    for i in list_of_numbers:
        if i%2 != 0:
            odd.append(i)
    return odd


# using list comprehension

def remove_even_li(list_of_num):
    return [num for num in list_of_num if num%2 != 0]

#print(remove_even([1,2,4,5,10,6,3,9]))
print(remove_even_li([1,2,4,5,10,6,3,9]))

