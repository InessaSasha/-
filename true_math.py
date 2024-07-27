from math import inf
def divide(first, second):
    if second == 0:
        return inf
    else:
       return (first / second)


result1 = divide(49, 7)
print(result1)
result2 = divide(15, 0)
print(result2)