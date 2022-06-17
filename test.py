def Funk(*args):
    for element in args:
        element += element + 1
    return element

print(Funk(3, 7, 4, 5))