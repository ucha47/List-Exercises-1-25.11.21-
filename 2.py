list1 = ["M", "na", "i", "Uc"]
list2 = ["y", "me", "s", "ha"]
list3 = [i + j for i, j in zip(list1, list2)]
print(list3)