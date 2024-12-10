def MaxList(liste : list) -> int:
    max_element = liste[0]
    for i in liste:
        if i > max_element: max_element = i
    return i

liste = [1, 2, 3, 4, 2, 3, -14, -12, 199, 250]
print(MaxList(liste))


