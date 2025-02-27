import numpy

def calculate_precision(a, b, classes):
    result = numpy.zeros(classes)
    for i in range(classes):
        tp = numpy.count_nonzero(a[a==i] == b[a==i])
        fp = numpy.count_nonzero(a[a==i] != b[a==i])
        print(tp, fp)
        result[i] = tp / (tp+fp) if (tp+fp) != 0 else 0

    return result

def calculate_recall(a, b, classes):
    result = numpy.zeros(classes)
    for i in range(classes):
        tp = numpy.count_nonzero(a[a==i] == b[a==i])
        fn = numpy.count_nonzero(a[b==i] != b[b==i])
        print(tp, fn)
        result[i] = tp / (tp+fn) if (tp+fn) != 0 else 0

    return result


classes = 5

a = numpy.random.randint(classes, size=20)
b = numpy.random.randint(classes, size=20)

print(a)
print(b)
epoch = calculate_precision(a, b, classes)
print(epoch)
epoch = calculate_recall(a, b, classes)
print(epoch)

