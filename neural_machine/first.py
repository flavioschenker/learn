import numpy

neurons = 8
max_path_length = 32
propagations = 1

self_mask = numpy.eye(neurons)
brain = numpy.random.randint(0,3, (neurons,neurons))
brain = numpy.exp(brain)
brain = brain*(1-self_mask)
brain = brain / numpy.expand_dims(numpy.sum(brain,axis=-1),axis=-1)
brain = brain.astype(numpy.float16)
print(brain)

neuron_activation = numpy.random.randint(0,10,neurons)
print(neuron_activation)
for i in range(propagations):
    neuron_activation = numpy.matmul(brain, neuron_activation)
    print(neuron_activation)