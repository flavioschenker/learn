#%%
import matplotlib.pyplot as plt
import numpy
x = numpy.arange(-5,5,step=0.01)
mean = 0
std = 1
y = (1 / (std*numpy.sqrt(2*numpy.pi))) * numpy.exp(-numpy.square((x - mean) / std) / 2)
plt.plot(x, y)
plt.xlabel='time (s)',
plt.ylabel='distribution (1)'
plt.title='About as simple as it gets, folks'
plt.show()
# %%
