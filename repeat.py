def repeat(s, n):
    for i in range(0):
        s+=s
    return s

print(repeat('*', 3)) # '***' 
print(repeat('abc', 2)) # 'abcabc' 
print(repeat('abc', 0)) # ''