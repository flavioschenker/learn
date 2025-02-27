import numpy

a = numpy.array([1,2,3,4,5,5,3,5,2,5,1,4,1,1,2,1])
n = 7
m = len(a)-n+1 # inklusive letzte
index = numpy.arange(n).reshape(1,-1) + numpy.arange(m).reshape(-1,1)
b = a[index]
print(b.shape)

# 1 = 5
# 2 = 3
# 3 = 1
# 4 = 2
# 5 = 4

c = b.reshape(m,1,n)
d = b.reshape(m,n,1)

print(c.shape)
print(d.shape)

e = c == d
f = numpy.count_nonzero(e, axis=-1)
g = numpy.argmax(f, axis=-1)
h = b[numpy.arange(m), g]
print(e.shape)
print(b)
print(f)
print(g)
print(h)