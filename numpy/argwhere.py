import numpy


a = numpy.array([1,2,3,4,5,8,3,2,2,2,2,2])

b = numpy.argwhere(a < 3).squeeze()
c = numpy.nonzero(a < 3)[0]

print(b)
print(c)