# def includes(l, v, i=0):
#     print(type(l))
#     while i < len(l):
#         if type(l) == dict and v in l.values() or (l[i] == v):
#             print(True)
#             return True
#         i+=1
#     print(False)
#     return False

def includes(l, v, i=0):
    if type(l) == dict and v in l.values():
        return True
    elif type(l) != dict and v in l[i::]: 
        return True
    return False

print(includes([1, 2, 3], 1)) # True 
print(includes([1, 2, 3], 1, 2)) # False 
print(includes({ 'a': 1, 'b': 2 }, 1)) # True 
print(includes({ 'a': 1, 'b': 2 }, 'a')) # False
print(includes('abcd', 'b')) # True
print(includes('abcd', 'e')) # False




