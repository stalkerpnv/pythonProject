def squared(x):
    return x**2
L = ['5', 18, '10', 13, '14']
L= list(map(int,L))
L =list(map(squared,L))
L = L[-1]
print(L)
