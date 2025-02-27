import numpy

neurons = 8
max_path_length = 32

# input hat bestimmte voltage
# signal propagiert linked-list mässig durch das gehirn
# bei jeder propagation wird voltage um eins verringert

brain = numpy.random.randint(0,2,(neurons,neurons))
brain = brain*(1-numpy.eye(neurons))
brain = brain.astype(numpy.uint8)
print(brain)

test_input = numpy.array([1,1,1,0,0,0,0,0])
neuron_voltage = max_path_length*test_input
neuron_voltage = (neuron_voltage - neuron_voltage.min()) / (neuron_voltage.max() - neuron_voltage.min())
print(neuron_voltage)

for i in range(max_path_length):
    neuron_voltage = numpy.matmul(brain, neuron_voltage)
    neuron_voltage = (neuron_voltage - neuron_voltage.min()) / (neuron_voltage.max() - neuron_voltage.min())
    print(neuron_voltage)
