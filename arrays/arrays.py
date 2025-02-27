# iterate over array
n = [1,2,3,4,5,6,7]

# with for range len
for i in range(len(n)):
    print(n[i])

# direct element
for elem in n:
    print(elem)

# both
for i, elem in enumerate(n):
    print(i, elem)

# access from the right (!len - 1 is important!)
for i in range(len(n)-1, -1, -1): # range(start, stop, increment)
    print(n[i])