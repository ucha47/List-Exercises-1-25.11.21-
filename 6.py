#  Exercise 6: Remove empty strings from the list of strings

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

#  first - manual way
#  list1.pop(1)
#  list1.pop(3)

res = list(filter(None, list1))

print(res)