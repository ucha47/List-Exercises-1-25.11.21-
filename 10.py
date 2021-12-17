#  Given a Python list, write a program to remove all occurrences of item 20.

list1 = [5, 20, 15, 20, 25, 50, 20]

#list comprehension
def remove_value(sample_list, value):
    return [i for i in sample_list if i != value]

res = remove_value(list1, 20)
print(res)